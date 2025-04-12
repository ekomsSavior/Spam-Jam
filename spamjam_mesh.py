import os
import sys
import time
import random
import subprocess
import argparse
from datetime import datetime
from bluepy.btle import Scanner, Peripheral, DefaultDelegate, ADDR_TYPE_RANDOM, BTLEException

# === Configuration ===
MESH_FILE = "mesh_nodes.txt"
MESH_BOT_PREFIX = "SpamJamMesh_"
CHAIN_REBROADCAST = False  # updated via --chain

# === Mesh Bot Registry ===
mesh_nodes = {}  # {mac: {"name": ..., "rssi": ..., "timestamp": ...}}

# === Banner ===
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

# === Save & Load ===
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

# === Scan + Add with Advanced Options ===
def scan_and_add():
    name_filter = input("🔤 Prefix to match (empty = all): ").strip()
    include_unnamed = input("❓ Include unnamed devices? (y/N): ").strip().lower() == "y"
    ask_each = input("❓ Ask before adding each device? (y/N): ").strip().lower() == "y"
    try:
        rssi_threshold = int(input("📶 Minimum RSSI (default -75): ") or -75)
    except:
        rssi_threshold = -75

    scanner = Scanner()
    print("🔍 Scanning...")
    try:
        devices = scanner.scan(10.0)
    except BTLEException as e:
        print(f"⚠️ Scan error: {e}")
        return

    added = 0
    for dev in devices:
        name = dev.getValueText(9) or "Unnamed"
        if dev.rssi < rssi_threshold:
            continue
        if name_filter and not name.startswith(name_filter):
            continue
        if name == "Unnamed" and not include_unnamed:
            continue
        if ask_each:
            choice = input(f"Add {dev.addr} ({name}, RSSI={dev.rssi})? [y/N]: ").strip().lower()
            if choice != "y":
                continue
        mesh_nodes[dev.addr] = {
            "name": name,
            "rssi": dev.rssi,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        print(f"✨ Added: {dev.addr} ({name})")
        added += 1

    save_mesh_nodes()
    print(f"✅ Added {added} new bot(s).")

# === Beacon Mode
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

# === Command Parser & Broadcast
def broadcast_command():
    if not mesh_nodes:
        print("⚠️ No bots to command! Load or scan first.")
        return
    print("\n📡 Bots:")
    for i, (mac, info) in enumerate(mesh_nodes.items()):
        print(f"  [{i}] {mac} ({info['name']}), RSSI={info['rssi']}")

    selection = input("💜 Select bot # or 'all': ").strip().lower()
    if selection == "all":
        targets = list(mesh_nodes.keys())
    else:
        try:
            idx = int(selection)
            targets = [list(mesh_nodes.keys())[idx]]
        except:
            print("⚠️ Invalid selection.")
            return

    message = input("💬 Enter mesh command (spam_mode, jam, scan): ").strip()
    chain = input("🔁 Chain this command to other bots? (y/N): ").strip().lower() == "y"

    for target in targets:
        try:
            print(f"📡 Connecting to {target}...")
            peripheral = Peripheral(target, ADDR_TYPE_RANDOM)
            peripheral.writeCharacteristic(0x0001, message.encode())
            print(f"✅ Sent '{message}' to {target}")
            if chain:
                print(f"🔁 [CHAIN] Repeating command to other nodes from {target}")
            peripheral.disconnect()
        except Exception as e:
            print(f"⚠️ Failed to send to {target}: {e}")

# === Main Menu
def main():
    print_banner()
    while True:
        print("\n🔹 1. Scan + Add Mesh Bots (Advanced Menu)")
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
