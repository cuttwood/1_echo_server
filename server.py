import socket

def main():
    host = '127.0.0.1'  # Локальный хост
    port = 12345  # Произвольный порт

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print("Сервер запущен...")
    conn, addr = server_socket.accept()
    print("Подключение установлено с", addr)

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("Получено от клиента:", data)
        conn.sendall(data.encode())

    conn.close()

if __name__ == '__main__':
    main()
