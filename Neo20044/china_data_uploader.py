import time
import random
import sys

def upload():
    files = ['passport.jpg', 'browser_history.txt', 'passwords.db', 'desktop_screenshot.png', 'bank_info.xlsx']
    servers = ['beijing.main.cn', 'shenzhen.node88.cn', 'wuhan.db-server.cn', 'guangzhou.transferhub.cn']

    print("Initializing secure connection to Chinese server...")
    time.sleep(2)

    server = random.choice(servers)
    print(f"Connected to {server} ✅")
    time.sleep(1.5)

    for file in files:
        print(f"Uploading {file} to {server}...")
        time.sleep(random.uniform(0.5, 1.5))
        print(f"{file} upload complete ✅")
        time.sleep(0.5)

    print("\nAll sensitive files successfully transferred to China.")
    print("感谢您的合作! (Thank you for your cooperation!) 🇨🇳💀")

if __name__ == "__main__":
    upload()
