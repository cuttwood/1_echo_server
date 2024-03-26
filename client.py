import socket

def main():
    host = '127.0.0.1'  # Локальный хост
    port = 12345  # Произвольный порт

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    message = input("Введите сообщение: ")
    client_socket.sendall(message.encode())

    data = client_socket.recv(1024).decode()
    print("Получено от сервера:", data)

    client_socket.close()

if __name__ == '__main__':
    main()
