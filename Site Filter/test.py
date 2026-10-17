from dnslib import DNSRecord
from config import LISTEN_PORT, UPSTREAM_DNS


def test_domain(domain):
    print(f"\nTesting: {domain}")

    query = DNSRecord.question(domain, "A")

    try:
        response = query.send(
            UPSTREAM_DNS,
            LISTEN_PORT,
            timeout=5
        )

        result = DNSRecord.parse(response)

        if result.header.rcode != 0:
            print(f"DNS error: {result.header.rcode}")
            return

        if result.rr:
            for answer in result.rr:
                print(f"Answer: {answer.rdata}")

                if str(answer.rdata) == "0.0.0.0":
                    print("RESULT: BLOCKED")
                else:
                    print("RESULT: DNS answer returned")
        else:
            print("No DNS answer returned.")

    except Exception as error:
        print(f"Request failed: {error}")


if __name__ == "__main__":
    test_domain("bet365.com")
    test_domain("google.com")
    test_domain("games.bet365.com")
