import socket
import logging


def setup_logger():
    # Создаем логгер
    logger = logging.getLogger('server_logger')
    logger.setLevel(logging.DEBUG)

    # Создаем обработчик для записи лога в файл
    file_handler = logging.FileHandler('server.log')
    file_handler.setLevel(logging.DEBUG)

    # Создаем форматтер
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Добавляем обработчик к логгеру
    logger.addHandler(file_handler)

    return logger


def main():
    logger = setup_logger()

    host = '127.0.0.1'  # Локальный хост
    port = 12345  # Произвольный порт

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    logger.info("Сервер запущен...")

    while True:
        conn, addr = server_socket.accept()
        logger.info(f"Подключение установлено с {addr}")

        try:
            while True:
                data = conn.recv(1024).decode()
                if not data:
                    break
                logger.info(f"Получено от клиента: {data}")
                conn.sendall(data.encode())
        finally:
            conn.close()


if __name__ == '__main__':
    main()
