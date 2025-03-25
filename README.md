# Spam-Jam  
📜 **Spam Jam — The Ultimate BLE & Bluetooth Attack Toolkit**  

**Author: ekoms savior 💜**  

🔥 Spam Jam is a powerful open-source Bluetooth attack toolkit designed for security researchers & ethical hackers.  

It features:  
✅ BLE Spamming 💌 (Send custom BLE spam messages)  
✅ BLE Jamming 🚫 (Overload BLE devices with junk packets)  
✅ L2Ping Attacks 💥 (Customizable Bluetooth ping flood)  
✅ RFCOMM Connection Flood 🔥 (Spam Bluetooth connections)  
✅ Full Bluetooth Device Scanning 📡  
✅ NEW!! Spam All BLE Devices 💌💥 (Send to *all* devices in range!)  
✅ NEW!! Jam All BLE Devices 🚫💥 (Jam *every* discovered device!)  
✅ NEW!! Auto Re-Scan + Re-Jam Loop 🔁 (Continuously detect and jam new devices)  
✅ NEW!! Real Time RSSI Filtering for Smarter Targeting 🧠 (Jam only strong signals!)

✅ NEW!! Introduced Classic Bluetooth discovery via hcitool scan

✅ NEW!! Increased BLE scan duration from 10s to 15s for improved detection

Built for research, security testing, and ethical hacking! 🚀💜

🛠️ Installation (Kali Linux)

Step 1: Clone the Repository

Open a terminal and run:

git clone https://github.com/ekomsSavior/Spam-Jam.git

cd Spam-Jam

Step 2: Install Dependencies

Before running Spam Jam, install required Bluetooth libraries:

sudo apt update && sudo apt install -y bluez bluez-tools python3-pip

sudo apt install python3-bluepy

Step 3: Run Spam Jam

sudo python3 spam_jam.py

🚨 Root is required for Bluetooth attacks! Always use sudo!

To UPDATE Spam Jam (run this while in the Spam Jam directory on your machine):

git pull

🎯 How to Use Spam Jam

When you run the tool, you’ll see this menu:

🔹 1️⃣ Spam a BLE device 💌

🔹 2️⃣ Jam a BLE device 🚫

🔹 3️⃣ Scan for Bluetooth devices 📡

🔹 4️⃣ L2Ping Attack 💥 (Now customizable!)

🔹 5️⃣ RFCOMM Connection Flood 💥

🔹 6️⃣ Start Bluetooth Service 📡

🔹 7️⃣ Quit 🚪

🛠️ Features & Usage Guide:

1️⃣ BLE Spam Attack (Send Custom Messages)

- Select option 1

- Enter the target BLE MAC address

- Type a custom spam message

- Press Enter to start spamming! 💥

2️⃣ BLE Jamming (Flood a BLE Device)

- Select option 2

- Enter the target BLE MAC address

- The tool will continuously send junk data to the device

3️⃣ Scan for Bluetooth Devices

- Select option 3

- The tool will scan for all nearby Bluetooth devices

- View MAC addresses & signal strength

4️⃣ L2Ping Attack (Bluetooth Ping Flood)

- Select option 4

- Enter the target device’s MAC address

- Enter packet size (default 600, max 672)

- Enable Flood Mode for continuous attack

- Watch as Spam Jam floods the device with Bluetooth pings! 💥

5️⃣ RFCOMM Connection Flood

- Select option 5

- Enter the target Bluetooth MAC address

- Spam Jam will attempt 1000+ RFCOMM connections

- May cause disconnections, slowdowns, or crashes! 💥

6️⃣ Start Bluetooth Service

- Select option 6

 -If Bluetooth isn’t running, this will start the service

7️⃣ Quit Spam Jam

- Select option 7 to exit


⚠️ Legal Disclaimer

This tool is for educational and research purposes only!

Using Spam Jam on networks or devices without permission is illegal. The creators are not responsible for any misuse. Be ethical!

💜 Contribute & Improve!

We welcome bug fixes, new features, and improvements!

💜 Fork the repo, submit PRs, and let’s build together!

🚀 LET'S SPAM & JAM!!!

Now go forth and HACK THE PLANET! 💜🔥


