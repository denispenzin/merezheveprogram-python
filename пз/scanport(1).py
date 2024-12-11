import socket

def scan_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1) 
            s.connect((host, port))  
            print(f"Порт {port} открыт")
    except (socket.timeout, ConnectionRefusedError):
        pass  

if __name__ == "__main__":
    target_host = "127.0.0.1" 
    for port in range(1, 1025): 
        scan_port(target_host, port)
