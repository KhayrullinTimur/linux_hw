import socket
from datetime import datetime

def main():
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.bind(("0.0.0.0", 1303))
	server_socket.listen(1)

	print("Сервер запущен и ожидает подключения")

	while True:
		client_socket, client_address = server_socket.accept()
		print(f"Подключено клиентом {client_address}")

		current_time = datetime.now().strftime("%d.%m.%Y %H:%M")
		client_socket.send(current_time.encode("utf-8"))

		client_socket.close()
		print(f"Соединение с {client_address} закрыто")

if __name__ == "__main__":
	main()


