from config import BLOCKLIST_FILE

def load_blocklist():
    with open(BLOCKLIST_FILE) as file:
        return{
            line.strip().lower()
            for line in file
        }

def is_blocked(domain, blocked_domains):
    return domain.lower() in blocked_domains