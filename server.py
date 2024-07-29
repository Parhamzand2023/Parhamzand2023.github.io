import socket
from send import Encryptor
def udp_server(ip, port):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((ip, port))
        print(f"Listening on {ip}:{port}")
        
        while True:
            data, addr = s.recvfrom(1024)  # دریافت داده‌ها (حداکثر 1024 بایت)
            message = data.decode()
            encryptor = Encryptor("jdupTCyJz9C-o0b3dwturSSxO9UtNOa5bljvLrJJmqw=")
            Text = encryptor.decrypt(message)
            if addr[0] == "192.168.56.1":
                name = "Parham"
            elif addr[0] == "192.168.56.1":
                name = "abol"
            print(f"{name}: {Text}")
            if Text == "exit":
                print("Shutting down server...")
                break

# اجرای سرور UDP
udp_server('0.0.0.0', 8080)
