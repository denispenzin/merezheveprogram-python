import socket

def echo_server(host='127.0.0.1', port=5000):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        print(f"Echo server запущено на {host}:{port}")

        server_socket.listen()
        print("Очікування з'єднань...")

        while True:
            conn, addr = server_socket.accept()
            with conn:
                print(f"Підключено до {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break  

                    print(f"Отримано: {data.decode('utf-8')}")
                    conn.sendall(data)
                    print(f"Відповідь надіслано")
if __name__ == "__main__":
    echo_server()
