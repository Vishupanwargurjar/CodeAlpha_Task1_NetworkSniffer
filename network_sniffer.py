from scapy.all import sniff

def packet_callback(packet):
    try:
        print("Source IP:", packet[0][1].src)
        print("Destination IP:", packet[0][1].dst)
        print("Protocol:", packet[0][1].proto)
        print("Payload:", bytes(packet[0][1].payload))
        print("-" * 50)
    except:
        pass

sniff(prn=packet_callback, count=10)
