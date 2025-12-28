import json
from datetime import datetime
from pathlib import Path

LOG_FILE = Path("logs/debate_log.jsonl")
LOG_FILE.parent.mkdir(exist_ok=True)

def log_event(event_type, payload):
    record = {
        "timestamp": datetime.utcnow().isoformat(),
        "event": event_type,
        "data": payload
    }
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")
