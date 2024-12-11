import socket

def echo_server(host='127.0.0.1', port=5000):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
            server_socket.bind((host, port))
            print(f"Echo server запущено на {host}:{port}")
            server_socket.listen()
            print("Очікування з'єднань...")

            while True:
                try:
                    conn, addr = server_socket.accept()
                    print(f"Підключено до {addr}")
                    handle_client(conn, addr)
                except Exception as client_error:
                    print(f"Помилка під час обробки клієнта: {client_error}")
    except OSError as os_error:
        print(f"Помилка сервера: {os_error}. Можливо, порт недоступний у цьому середовищі.")

def handle_client(conn, addr):
    with conn:
        while True:
            try:
                data = conn.recv(1024)
                if not data:
                    print(f"З'єднання з {addr} закрито")
                    break 
                print(f"Отримано від {addr}: {data.decode('utf-8')}")
                conn.sendall(data)
                print(f"Відповідь надіслано {addr}")
            except Exception as e:
                print(f"Помилка при обробці даних від {addr}: {e}")
                break

if __name__ == "__main__":
    echo_server()
