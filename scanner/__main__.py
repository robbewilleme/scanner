import argparse
from host_discovery import discover_hosts
from service_discovery import portscan



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ip', type=str, required=True)
    parser.add_argument('-p', action='store_true')
    args = parser.parse_args()

    hosts = discover_hosts(args.ip)
    
    if args.p:
        for host in hosts:
            open_ports = portscan(host)
            print(host)
            print(open_ports)
    else:
        print(hosts)


if __name__ == "__main__":
    main()