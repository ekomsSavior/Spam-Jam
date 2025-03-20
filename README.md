# Spam-Jam
📜 Spam Jam — The Ultimate BLE & Bluetooth Attack Toolkit
Author: ekoms savior 💜

🔥 Spam Jam is a powerful open-source Bluetooth attack toolkit designed for security researchers & ethical hackers.
It features:
✅ BLE Spamming 💌 (Send custom BLE spam messages)
✅ BLE Jamming 🚫 (Overload BLE devices with junk packets)
✅ L2Ping Attacks 💥 (Customizable Bluetooth ping flood)
✅ RFCOMM Connection Flood 🔥 (Spam Bluetooth connections)
✅ Full Bluetooth Device Scanning 📡

Built for research, security testing, and ethical hacking! 🚀💜

🛠️ Installation (Kali Linux)
Step 1: Clone the Repository
Open a terminal and run:

git clone https://github.com/ekomsSavior/Spam-Jam.git

cd spam-jam

Step 2: Install Dependencies
Before running Spam Jam, install required Bluetooth libraries:

sudo apt update && sudo apt install -y bluez bluez-tools python3-pip

pip3 install bluepy

Step 3: Run Spam Jam

sudo python3 spam_jam.py
🚨 Root is required for Bluetooth attacks! Always use sudo!

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
1️⃣ Select option 1
2️⃣ Enter the target BLE MAC address
3️⃣ Type a custom spam message
4️⃣ Press Enter to start spamming! 💥

2️⃣ BLE Jamming (Flood a BLE Device)
1️⃣ Select option 2
2️⃣ Enter the target BLE MAC address
3️⃣ The tool will continuously send junk data to the device

3️⃣ Scan for Bluetooth Devices
1️⃣ Select option 3
2️⃣ The tool will scan for all nearby Bluetooth devices
3️⃣ View MAC addresses & signal strength

4️⃣ L2Ping Attack (Bluetooth Ping Flood)
1️⃣ Select option 4
2️⃣ Enter the target device’s MAC address
3️⃣ Enter packet size (default 600, max 672)
4️⃣ Enable Flood Mode for continuous attack
5️⃣ Watch as Spam Jam floods the device with Bluetooth pings! 💥

5️⃣ RFCOMM Connection Flood
1️⃣ Select option 5
2️⃣ Enter the target Bluetooth MAC address
3️⃣ Spam Jam will attempt 1000+ RFCOMM connections
4️⃣ May cause disconnections, slowdowns, or crashes! 💥

6️⃣ Start Bluetooth Service
1️⃣ Select option 6
2️⃣ If Bluetooth isn’t running, this will start the service

7️⃣ Quit Spam Jam
1️⃣ Select option 7 to exit

⚠️ Legal Disclaimer
This tool is for educational and research purposes only!
Using Spam Jam on networks or devices without permission is illegal. The creators are not responsible for any misuse. Be ethical!

💜 Contribute & Improve!
We welcome bug fixes, new features, and improvements!
💜 Fork the repo, submit PRs, and let’s build together!

🚀 LET'S SPAM & JAM!!!
Now go forth and HACK THE PLANET! 💜🔥


