import socket
import threading

def scan_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            s.connect((host, port))
            print(f"[+] Порт {port} открыт")
    except:
        pass 

def start_scan(host, ports):
    threads = []
    for port in ports:
        thread = threading.Thread(target=scan_port, args=(host, port))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()  

if __name__ == "__main__":
    target_host = input("Введите IP-адрес цели: ")
    ports_to_scan = range(1, 1025)  

    print(f"Запуск сканирования на хосте {target_host}...")
    start_scan(target_host, ports_to_scan)
    print("Сканирование завершено!")
