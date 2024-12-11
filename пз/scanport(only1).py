import socket

def check_single_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            s.connect((host, port))
            print(f"Порт {port} открыт")
    except:
        print(f"Порт {port} закрыт")

if __name__ == "__main__":
    target_host = input("Введите IP-адрес: ")
    target_port = int(input("Введите номер порта: "))

    check_single_port(target_host, target_port)
