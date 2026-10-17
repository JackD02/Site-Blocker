from filter import load_blocklist
from dns_server import start_server


def main():
    print("==========================")
    print(" ")
    print(" SITE FILTER ")
    print(" ")
    print("==========================")

    blocked_domains = load_blocklist()

    try:
        start_server(blocked_domains)

    except KeyboardInterrupt:
        print("\nDNS server stopped.")

    except Exception as error:
        print(f"An error occurred: {error}")

if __name__ == "__main__":
    main()
