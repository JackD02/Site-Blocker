from config import BLOCKLIST_FILE

def load_blocklist():
    with open(BLOCKLIST_FILE, "r", encoding="utf-8") as file:
        return{
            line.strip().lower().rstrip(".")
            for line in file
            if line.strip() and not line.lstrip().startswith("#")
        }

def is_blocked(domain, blocked_domains):
    domain =  domain.lower().rstrip(".")

    return any(
        domain == blocked
        or domain.endswith("." + blocked)
        for blocked in blocked_domains
)
