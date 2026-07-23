from filter import load_blocklist
from dns_server import start_server

blocked_domains = load_blocklist()

start_server(blocked_domains)