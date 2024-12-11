import socket

def echo_client(host='127.0.0.1', port=5000):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        print(f"Підключено до сервера {host}:{port}")
        try:
            while True:
                message = input("Введіть повідомлення для надсилання (або 'exit' для виходу): ")
                if message.lower() == 'exit':
                    print("Завершення роботи клієнта...")
                    break
                client_socket.sendall(message.encode('utf-8'))
                data = client_socket.recv(1024)
                print(f"Відповідь від сервера: {data.decode('utf-8')}")
        except KeyboardInterrupt:
            print("Клієнт примусово завершено")
if __name__ == "__main__":
    echo_client()
