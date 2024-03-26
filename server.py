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

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print("Сервер запущен...")

    while True:
        conn, addr = server_socket.accept()
        print("Подключение установлено с", addr)

        try:
            while True:
                data = conn.recv(1024).decode()
                if not data:
                    break
                print("Получено от клиента:", data)
                conn.sendall(data.encode())
        finally:
            conn.close()


if __name__ == '__main__':
    main()
