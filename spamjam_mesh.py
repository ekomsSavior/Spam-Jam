# spamjam_mesh.py
import os
import sys
import time
import random
import subprocess
import argparse
from datetime import datetime
from bluepy.btle import Scanner, Peripheral, DefaultDelegate, ADDR_TYPE_RANDOM, BTLEException

MESH_FILE = "mesh_nodes.txt"
MESH_BOT_PREFIX = "SpamJamMesh_"
CHAIN_REBROADCAST = False
mesh_nodes = {}

def print_banner():
    print(r"""
███████╗██████╗  █████╗ ███╗   ███╗         ██╗ █████╗ ███╗   ███╗
██╔════╝██╔══██╗██╔══██╗████╗ ████║         ██║██╔══██╗████╗ ████║
███████╗██████╔╝███████║██╔████╔██║         ██║███████║██╔████╔██║
╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║    ██   ██║██╔══██║██║╚██╔╝██║
███████║██║     ██║  ██║██║ ╚═╝ ██║    ╚█████╔╝██║  ██║██║ ╚═╝ ██║
╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝     ╚════╝ ╚═╝  ╚═╝╚═╝     ╚═╝ 
🌐 BLE MESH MODE – Spam Jam Network 🌐
by ekoms savior 💜 xoxoxo
""")

def save_mesh_nodes():
    with open(MESH_FILE, "w") as f:
        for mac, info in mesh_nodes.items():
            f.write(f"{mac},{info['name']},{info['rssi']},{info['timestamp']}\n")
    print("💾 Saved mesh bot info to mesh_nodes.txt")

def load_mesh_nodes():
    if not os.path.exists(MESH_FILE):
        print("⚠️ No mesh_nodes.txt found.")
        return
    mesh_nodes.clear()
    with open(MESH_FILE, "r") as f:
        for line in f:
            try:
                mac, name, rssi, timestamp = line.strip().split(",", 3)
                mesh_nodes[mac] = {"name": name, "rssi": rssi, "timestamp": timestamp}
            except:
                continue
    print(f"📂 Loaded {len(mesh_nodes)} mesh bots from file.")

# === Scan + Add
def scan_and_add():
    print("\n🔍 ADVANCED SCAN MODE – Let's find those bots!")

    name_filter = input("🔤 Prefix to match (empty = all): ").strip()
    include_unnamed = input("❓ Include unnamed devices? (y/N): ").strip().lower() == "y"
    ask_each = input("❓ Ask before adding each device? (y/N): ").strip().lower() == "y"

    try:
        rssi_threshold = int(input("📶 Minimum RSSI (default -75): ") or -75)
    except ValueError:
        rssi_threshold = -75

    try:
        rounds = int(input("🔁 How many scan passes? (default 1): ") or 1)
    except ValueError:
        rounds = 1

    scanner = Scanner()
    found_devices = {}

    for round_num in range(rounds):
        print(f"📡 Scan Pass {round_num + 1} of {rounds}...")
        try:
            devices = scanner.scan(15.0)
        except BTLEException as e:
            print(f"⚠️ BLE scan error: {e}")
            continue

        for dev in devices:
            mac = dev.addr
            name = dev.getValueText(9) or "Unnamed"
            rssi = dev.rssi

            if rssi < rssi_threshold:
                continue
            if name_filter and not name.startswith(name_filter):
                continue
            if name == "Unnamed" and not include_unnamed:
                continue
            if mac in mesh_nodes or mac in found_devices:
                continue

            if ask_each:
                choice = input(f"🧠 Add {mac} ({name}, RSSI={rssi})? [y/N]: ").strip().lower()
                if choice != "y":
                    continue

            found_devices[mac] = {
                "name": name,
                "rssi": rssi,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            print(f"✨ Added: {mac} ({name}, RSSI={rssi})")

    mesh_nodes.update(found_devices)
    if found_devices:
        save_mesh_nodes()
        print(f"\n✅ Total new mesh bots added: {len(found_devices)}")
    else:
        print("⚠️ No new matching devices found.")

def become_mesh_bot():
    name = f"{MESH_BOT_PREFIX}{random.randint(1000,9999)}"
    print(f"📡 Advertising as {name}... Ctrl+C to stop.")
    try:
        subprocess.run(["bluetoothctl", "power", "on"], stdout=subprocess.DEVNULL)
        subprocess.run(["bluetoothctl", "discoverable", "on"], stdout=subprocess.DEVNULL)
        subprocess.run(["bluetoothctl", "pairable", "on"], stdout=subprocess.DEVNULL)
        subprocess.run(["bluetoothctl", "agent", "NoInputNoOutput"], stdout=subprocess.DEVNULL)
        while True:
            subprocess.run(["bluetoothctl", "system-alias", name], stdout=subprocess.DEVNULL)
            time.sleep(2)
    except KeyboardInterrupt:
        subprocess.run(["bluetoothctl", "system-alias", "SpamJam"], stdout=subprocess.DEVNULL)
        print("🛑 Beacon mode stopped.")

def broadcast_command():
    if not mesh_nodes:
        print("⚠️ No bots to command! Load or scan first.")
        return

    print("\n📡 Bots:")
    for i, (mac, info) in enumerate(mesh_nodes.items()):
        print(f"  [{i}] {mac} ({info['name']}), RSSI={info['rssi']}")

    selection = input("💜 Select bot # or 'all': ").strip().lower()
    targets = []
    if selection == "all":
        targets = list(mesh_nodes.keys())
    else:
        try:
            idx = int(selection)
            targets = [list(mesh_nodes.keys())[idx]]
        except:
            print("⚠️ Invalid selection.")
            return

    message = input("💬 Enter mesh command (scan_spam / scan_jam): ").strip()
    chain = input("🔁 Chain this command to other bots? (y/N): ").strip().lower() == "y"

    try:
        while True:
            for target in targets:
                try:
                    print(f"📡 Connecting to {target}...")
                    peripheral = Peripheral(target, ADDR_TYPE_RANDOM)
                    peripheral.writeCharacteristic(0x0001, message.encode())
                    print(f"✅ Sent '{message}' to {target}")
                    if chain:
                        print(f"🔁 [CHAIN] Message will be rebroadcast by bot.")
                    peripheral.disconnect()
                except Exception as e:
                    print(f"⚠️ Failed to send to {target}: {e}")
            scan_and_add()  # Continuous auto-growth
            print("🌀 Waiting 10s to protect bots...")
            time.sleep(10)
    except KeyboardInterrupt:
        print("🛑 Loop stopped by user.")

def main():
    print_banner()
    while True:
        print("\n🔹 1. Scan + Add Mesh Bots")
        print("🔹 2. Load Saved Mesh Bots")
        print("🔹 3. Broadcast Command to Bots")
        print("🔹 4. Become a Mesh Bot (Beacon Mode)")
        print("🔹 5. Quit")
        choice = input("💜 Choose an option (1-5): ").strip()
        if choice == "1":
            scan_and_add()
        elif choice == "2":
            load_mesh_nodes()
        elif choice == "3":
            broadcast_command()
        elif choice == "4":
            become_mesh_bot()
        elif choice == "5":
            print("👋 Bye fren! xoxo 💜")
            break
        else:
            print("⚠️ Invalid choice!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--chain", action="store_true", help="Enable message rebroadcasting on mesh bots")
    args = parser.parse_args()
    CHAIN_REBROADCAST = args.chain
    main()
