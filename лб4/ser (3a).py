import socket

def echo_server(host='127.0.0.1', port=5000):
    try:
         with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
            
            server_socket.bind((host, port))
            print(f"File server запущено на {host}:{port}")

            server_socket.listen()
            print("Очікування з'єднань...")

            while True:
                try:
                    conn, addr = server_socket.accept()
                    print(f"Підключено до {addr}")
                    receive_file(conn, addr)
                except Exception as client_error:
                    print(f"Помилка під час обробки клієнта: {client_error}")
    except OSError as os_error:
        print(f"Помилка сервера: {os_error}. Можливо, порт недоступний у цьому середовищі.")

def receive_file(conn, addr):
    try:
        with conn:
            filename = conn.recv(1024).decode('utf-8')
            print(f"Отримання файлу: {filename} від {addr}")
            with open(f"received_{filename}", 'wb') as f:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    f.write(data)
            print(f"Файл {filename} успішно отримано та збережено як received_{filename}")
    except Exception as e:
        print(f"Помилка під час отримання файлу: {e}")

if __name__ == "__main__":
    echo_server()
