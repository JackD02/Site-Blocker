from datetime import datetime
from config import LOG_FILE

def log_block(domain):
    timestamp = datetime.now()

    with open(LOG_FILE, "a") as file:
        file.write(f"{timestamp}: {domain}\n")