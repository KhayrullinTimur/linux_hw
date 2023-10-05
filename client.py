import socket

def main():
	server_ip = "0.0.0.0"
	server_port = 1303
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	try:
		client_socket.connect((server_ip, server_port))
		print("Подключено к серверу")

		response = client_socket.recv(1024)
		print(f"Получено от сервера: {response.decode('utf-8')}")

	except ConnectionRefusedError:
		print("Не удалось подключиться к серверу")
	except Exception as e:
		print(f"Произошла ошибка при подключении: {str(e)}")
	finally:
		client_socket.close()

if __name__ == "__main__":
	main()
