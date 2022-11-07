import random
from scapy.all import IP, sr1, sr, TCP
import sys

def portscan(host):
    open_ports = []
    for target_port in range(100):
        src_port = random.randint(1025,65534)
        response = sr1(
            IP(dst=host)/TCP(sport=src_port, dport=target_port,flags="S"), timeout=0.1,
            verbose=0
        )
        if response is not None:
            if(response.haslayer(TCP)):
                if(response.getlayer(TCP).flags == 0x12):
                    send_rst = sr(
                        IP(dst=host)/TCP(sport=src_port,dport=target_port,flags='R'),
                        timeout=1,
                        verbose=0
                    )
                    open_ports.append(target_port)   
    return open_ports
    

def main():
    target_ip = sys.argv[1]
    ports = portscan(target_ip)
    print(ports)

if __name__ == "__main__":
    main()
