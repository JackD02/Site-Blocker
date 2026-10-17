from pathlib import Path

BLOCKLIST_FILE = Path(__file__).parent / "Data" / "blocked.txt"

LOG_FILE = "logs.txt"

UPSTREAM_DNS = "127.0.0.1" # "1.1.1.1" for actual "127.0.0.1" for test

LISTEN_PORT = 8053 #53 for actual 8053 for testing
