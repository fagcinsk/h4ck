#!/usr/bin/env python3

"""
ScaPy dns sniffer
"""

from scapy.all import DNSQR, sniff, DNS


def pkt_recv(pkt):
    if pkt.haslayer(DNSQR):
        print(pkt[DNS].qd.qname.decode())


if __name__ == "__main__":
    sniff(iface='wlan0', prn=pkt_recv, store=0, filter="udp port 53")
