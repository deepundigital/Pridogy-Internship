from scapy.all import sniff, IP, Raw

def packet_callback(packet):
    if IP in packet:
        ip_layer = packet[IP]
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        protocol = ip_layer.proto

        print(f"\nSource IP: {src_ip}")
        print(f"Destination IP: {dst_ip}")
        print(f"Protocol: {protocol}")

        # Check if payload exists
        if Raw in packet:
            payload = packet[Raw].load
            print(f"Payload: {payload}")

def main():
    print("Starting packet capture. Press Ctrl+C to stop.")
    # Capture packets indefinitely
    sniff(prn=packet_callback, store=False)

if __name__ == "__main__":
    main()
