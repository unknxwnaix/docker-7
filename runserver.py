import socket
import os


def get_local_ip():
    try:
        # Определяем IP-адрес устройства в локальной сети
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception as e:
        print(f"Ошибка определения локального IP: {e}")
        return "127.0.0.1"


if __name__ == "__main__":
    ip = get_local_ip()
    port = 8080  # Укажите желаемый порт
    print(f"Запуск сервера Django на {ip}:{port}")
    os.system(f"python manage.py runserver {ip}:{port}")
