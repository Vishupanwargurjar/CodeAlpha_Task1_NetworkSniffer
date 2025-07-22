from scapy.all import sniff, IP, TCP, UDP
from datetime import datetime

# Simple function to process and display each packet
def process_packet(packet):
    try:
        # Time of capture
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Extract IP layer
        if IP in packet:
            src = packet[IP].src
            dst = packet[IP].dst
            proto = packet[IP].proto

            # Default port values
            sport = dport = "-"

            # Check protocol
            if TCP in packet:
                sport = packet[TCP].sport
                dport = packet[TCP].dport
                protocol = "TCP"
            elif UDP in packet:
                sport = packet[UDP].sport
                dport = packet[UDP].dport
                protocol = "UDP"
            else:
                protocol = "Other"

            # Format output
            log = f"[{timestamp}] {protocol} Packet: {src}:{sport} -> {dst}:{dport}"
            print(log)

            # Save to file
            with open("sniffed_packets.txt", "a") as f:
                f.write(log + "\n")
    except Exception as e:
        print(f"Error processing packet: {e}")

# Start sniffing
print("Sniffing started on interface 'en0'... Press Ctrl+C to stop.")
sniff(prn=process_packet, store=False, iface="en0")  # 👈 Use 'en0' for Mac Wi-Fi
