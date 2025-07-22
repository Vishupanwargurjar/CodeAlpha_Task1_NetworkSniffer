# 🛡️ Network Packet Sniffer using Scapy

This is a simple Python project I created for **CodeAlpha Cybersecurity Internship - Task 1**.  
It captures network packets live from my system and prints important details like source, destination, protocol, and ports. It also saves all captured packets in a text file.

---

## ✅ Features

- Captures live network packets using Scapy
- Shows both TCP and UDP packets
- Works on a specific network interface (like `en0` on Mac)
- Adds timestamps to each captured packet
- Saves the output to a file: `sniffed_packets.txt`

---

## 📦 Requirements

- Python 3
- Scapy library

Install Scapy using:

```bash
pip install scapy

How to Run :-
sudo python3 network_sniffer_simple.py
