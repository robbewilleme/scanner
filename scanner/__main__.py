import argparse
from host_discovery import discover_hosts
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ip', type=str, required=True)
    args = parser.parse_args()

    hosts = discover_hosts(args.ip)
    print(hosts)


if __name__ == "__main__":
    main()