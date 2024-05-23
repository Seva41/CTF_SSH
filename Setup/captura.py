# CTF 1 - Seguridad en TI 2024/1 - UAI Viña del Mar
# Autor: Sebastián Dinator - https://github.com/Seva41
# Abril 2024

import random
from scapy.all import *


# Function to generate random IPs
def random_ip():
    return ".".join(str(random.randint(1, 254)) for _ in range(4))


if __name__ == "__main__":
    # Define packet data
    packets = []

    # Generate a large number of random packets including HTTP, DNS, ICMP, ARP, and SSL/TLS
    for _ in range(100):  # Adjust count for desired traffic volume
        # Simulate DNS Queries
        dns = random.choice(["www.uai.cl", "www.google.com", "www.webc.uai.cl"])
        dns_packet = (
            Ether()
            / IP(src=random_ip(), dst="8.8.8.8")
            / UDP(dport=53)
            / DNS(rd=1, qd=DNSQR(qname=dns))
        )
        packets.append(dns_packet)

        # Simulate regular HTTP traffic
        host = random.choice(["www.uai.cl", "www.google.com", "www.webc.uai.cl"])
        regular_http = f"GET /index.html HTTP/1.1\\r\\nHost: {host}\\r\\n\\r\\n"
        http_packet = (
            Ether() / IP(src=random_ip(), dst=random_ip()) / TCP() / regular_http
        )
        packets.append(http_packet)

        # Simulate ICMP Ping requests
        icmp_packet = Ether() / IP(src=random_ip(), dst=random_ip()) / ICMP()
        packets.append(icmp_packet)

        # Simulate ARP requests
        arp_packet = Ether() / ARP(pdst=random_ip(), psrc=random_ip())
        packets.append(arp_packet)

        # Simulate SSL/TLS traffic
        ssl_host = random.choice(["www.uai.cl", "www.google.com", "www.webc.uai.cl"])
        ssl_packet = (
            Ether()
            / IP(src=random_ip(), dst=random_ip())
            / TCP(dport=443)
            / Raw(load="Client Hello")
        )
        packets.append(ssl_packet)

    # Insert credential packets at random positions
    credentials = [
        ("Usuario: server ", "Pass: admin1 "),
        ("Usuario: ctfuser ", "Pass: secure123# "),
        ("Usuario: admin ", "Pass: password "),
    ]
    for user, password in credentials:
        headers = f"GET / HTTP/1.1\\r\\nHost: www.example.com\\r\\n"
        auth = f"Authorization: Basic {user}:{password}\\r\\n\\r\\n"
        credential_packet = (
            Ether() / IP(src=random_ip(), dst="192.168.0.1") / TCP() / (headers + auth)
        )
        insert_pos = random.randint(0, len(packets))
        packets.insert(insert_pos, credential_packet)

    # Write the packets to a pcap file
    wrpcap("conexion.pcap", packets)

    print("El tráfico de red ha sido capturado. Se ha generado un archivo.")
