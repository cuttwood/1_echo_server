import socket

def main():
    host = '127.0.0.1'  # Локальный хост
    port = 12345  # Произвольный порт

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

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
