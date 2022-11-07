from host_discovery import discover_hosts
import sys



def main():
    hosts = discover_hosts(sys.argv[1])
    print(hosts)


if __name__ == "__main__":
    main()