Spam-Jam

 Spam Jam — The Ultimate BLE & Bluetooth Attack Toolkit

Author: ekoms savior 
 Now featuring a BLE Mesh Botnet 

![image4](https://github.com/user-attachments/assets/bb71fb71-3259-4a0e-80a2-15df607eaaca)

 Spam Jam is a powerful, open-source Bluetooth attack toolkit 

It features:

 BLE Spamming  (Send custom BLE spam messages)

 BLE Jamming  (Overload BLE devices with junk packets)

 L2Ping Attacks  (Bluetooth ping flood)

 RFCOMM Flood  (Spam Bluetooth connections)

Full Bluetooth Device Scanning 

NEW BLE MESH BOTNET SYSTEM

 Mesh Botnet Mode – Broadcast commands across BLE bots

 Beacon Mode – Turn any device into a mesh node

 Real-Time Scanning + Bot Discovery

Persistent mesh_nodes.txt file (MAC, Name, RSSI, Timestamp)

 Optional Recursive Chaining – Bots rebroadcast messages
Command Parsing: spam_mode, jam, scan, chain, etc.

 Self-Growing – Bots scan for and save new bots

 Continuous Broadcast Loop Mode

 Extend range using chained bots over time

 Full mesh registry stored for easy editing

 Installation (Kali Linux)

Step 1: Clone the Repository

git clone https://github.com/ekomsSavior/Spam-Jam.git

cd Spam-Jam

Step 2: Install Dependencies

sudo apt update && sudo apt install -y bluez bluez-tools python3-pip

sudo apt install python3-bluepy

Step 3: Run Spam Jam

sudo python3 spam_jam.py

 Root is required for Bluetooth attacks! Always use sudo.

To update Spam Jam at any time:

git pull


 Menu (Current Version)

🔹 0 BLE Advertise All 

🔹 1 Start Bluetooth Service 

🔹 2 Scan for Bluetooth devices 

🔹 3 Spam a BLE device 

🔹 4 Spam All BLE Devices 

🔹 5 Jam a BLE device 

🔹 6 Jam All BLE Devices 

🔹 7 Mesh Network Menu 

🔹 8 L2Ping Attack 

🔹 9 RFCOMM Flood 

🔹 10 Quit 

 Mesh Network Menu ( Option 7)

The BLE Mesh Botnet is Spam Jam's secret weapon.

Any BLE device can become a mesh bot. These bots

Broadcast their presence with a custom alias (e.g. SpamJamMesh_XXXX)

Receive & execute mesh commands: spam_mode, jam, scan

Optionally rebroadcast commands to extend the network!

mesh menu options 

🔹 1. Scan + Add Mesh Bots (Advanced Menu)

🔹 2. Load Saved Mesh Bots

🔹 3. Broadcast Command to Bots

🔹 4. Become a Mesh Bot (Beacon Mode)

🔹 5. Quit

 Scanning gives you full control — filter by name, RSSI, Scan in sequence and more.

 Saved bots are written to mesh_nodes.txt with MAC, name, RSSI, and timestamp.

 Commands sent to bots are delivered via BLE write and executed based on the message.

 Command Examples for Mesh Bots

After selecting a bot or "all", enter a command

spam_mode → Performs BLE spamming to nearby devices

jam → Sends random junk packets (BLE jamming)

scan → Scans for more nearby bots to grow the mesh

chain → Repeats this command to other bots it discovers 

 This allows mass coordination of BLE attacks with no central C2. Each bot becomes a repeater!

 Experiment Ideas for Advanced Users

Turn your entire lab into a BLE botnet swarm using old phones, Raspberry Pis, or dongles

Create rogue mesh nodes pretending to be real IoT devices

Use scan + chain to recursively map a BLE landscape

Attach physical GPS or CSI logging to beacon nodes for BLE signal analysis

Write your own mesh command payloads (future extensibility coming!)

EXTRA SPAM-JAM FEATURES:  mesh_bot_listener.py

This script turns your BLE device into an active mesh bot listener.

Setup Instructions:

1. Open the file in a text editor.

2. Replace the `TARGET_MAC` value with the MAC address of the device you want to connect to.

3. Run the script with:

   sudo python3 mesh_bot_listener.py

What it does:

 Listens for incoming BLE mesh commands like `scan`, `scan_jam`, or `scan_spam`

 Executes them in real time

 Can be run on Raspberry Pis, laptops, or other BLE-capable gear

This tool is optional, but helpful if you're building a physical mesh of devices and want each node to act automatically on received commands.

!!Make sure the MAC is part of your mesh_nodes.txt file!!


 Legal Disclaimer

Spam Jam is for educational and research use only.

Unauthorized use on networks or devices you do not own is illegal.

Pull requests welcome!

Build with me at: https://github.com/ekomsSavior

FOllOW me on IG: https://instagram.com/ekoms.is.my.savior

Read my articles over at MEDIUM: https://medium.com/@ekoms1
