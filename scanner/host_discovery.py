from scapy.all import ARP, Ether, srp
import sys

def discover_hosts(ip):
    arp = ARP(pdst=ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp
    result = srp(packet, timeout=3)[0]
    hosts = []
    for sent, received in result:
        hosts.append(received.psrc)
    return hosts


def main():
    target_ip = sys.argv[1]
    active_hosts = discover_hosts(target_ip)
    print(active_hosts)

if __name__ == "__main__":
    main()
