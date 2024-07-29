import socket
import sys
from cryptography.fernet import Fernet
from termcolor import colored
class color:
    @classmethod
    # نوشتن موفقیت آمیز بودن
    def green(cls, text):
        print(colored(text, "green"))
    @classmethod
    # نوشتن خطا ها 
    def red(cls, text):
        print(colored(text, "red"))
class Encryptor:
    def __init__(self, key=None):
        try:
            if key is None:
                self.key = Fernet.generate_key()
            else:
                self.key = key.encode()  # تبدیل کلید به بایت
            self.cipher = Fernet(self.key)
        except:
            color.red("( ͡─ ͜ʖ ͡─) 👉 The app has a programming or security bug")
            sys.exit()
    
    def encrypt(self, message):
        try:
            return self.cipher.encrypt(message.encode()).decode()  # تبدیل به رشته برای نمایش
        except:
            color.red("( ͡─ ͜ʖ ͡─) 👉 The app has a programming or security bug")
            sys.exit()
    def decrypt(self, encrypted_message):
        return self.cipher.decrypt(encrypted_message.encode()).decode()  # تبدیل ورودی به بایت
def encrypt___init_(Text):
    # ایجاد یک کلید جدید
    try: 
        key = "jdupTCyJz9C-o0b3dwturSSxO9UtNOa5bljvLrJJmqw="
        encryptor = Encryptor(key)
        encrypted_message = encryptor.encrypt(Text)

        return encrypted_message
    except:
        color.red("( ͡─ ͜ʖ ͡─) 👉 The app has a programming or security bug")
        sys.exit()
def send_data_udp(ip, port, data):
    # ایجاد یک سوکت UDP
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        # ارسال داده
        s.sendto(data.encode(), (ip, port))

def main(ip):
    # استفاده از تابع
    while True:
        try:
            send_data_udp(ip, 8080, encrypt___init_(input("Enter your Text: ")))
        except KeyboardInterrupt:
            break
        except EOFError:
            break

if __name__ == "__main__":
    ip = input("Enter your IP: ")
    main(ip)
