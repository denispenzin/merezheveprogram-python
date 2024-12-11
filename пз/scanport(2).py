import socket

def scan_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            s.connect((host, port))
            print(f"[+] Порт {port} открыт")
    except:
        print(f"[-] Порт {port} закрыт")

if __name__ == "__main__":
    target = input("Введите IP-адрес для сканирования: ")
    ports = range(1, 1025) 

    print(f"Сканирование хоста {target}...")
    for port in ports:
        scan_port(target, port)