from dnslib.server import DNSServer, BaseResolver
from dnslib import DNSRecord, RR, A

from filter import is_blocked
from logger import log_block
from config import UPSTREAM_DNS, LISTEN_PORT

upstream_dns = UPSTREAM_DNS

class FilterResolver(BaseResolver):

    def __init__(self, blocked_domains):
        self.blocked_domains = blocked_domains

    def resolve(self, request):

        domain = str(request.q.qname).rstrip(".").lower()

        print(f"Request for {domain}")

        if is_blocked(domain, self.blocked_domains):
            log_block(domain)

        reply = request.reply()

        reply.add_answer(
            RR(domain, rdata=("0.0.0.0"))
        )

    def forward_request(self, request):
        response = DNSRecord.parse( request.send(upstream_dns, LISTEN_PORT)) #53 for actual 8053 for testing

        return response

def start_server(blocked_domains):
    resolver = FilterResolver(blocked_domains)

    server = DNSServer(
        resolver,
        address="0.0.0.0",
        port = LISTEN_PORT #53 for actual 8053 for testing
    )

    print("Server starting")

    server.start()
