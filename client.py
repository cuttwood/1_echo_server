import socket


def main():
    default_host = '127.0.0.1'  # Значение по умолчанию для хоста
    default_port = 12345  # Значение по умолчанию для порта

    host = input(f"Введите хост (по умолчанию {default_host}): ") or default_host
    port_str = input(f"Введите порт (по умолчанию {default_port}): ") or str(default_port)

    try:
        port = int(port_str)
    except ValueError:
        print("Ошибка: порт должен быть целым числом.")
        return

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((host, port))
    except ConnectionRefusedError:
        print("Ошибка: соединение отклонено. Убедитесь, что сервер запущен и доступен по указанным хосту и порту.")
        return

    try:
        while True:
            message = input("Введите сообщение (или 'exit' для выхода): ")
            client_socket.sendall(message.encode())
            if message == "exit":
                break
            data = client_socket.recv(1024).decode()
            print("Получено от сервера:", data)
    finally:
        client_socket.close()


if __name__ == '__main__':
    main()
