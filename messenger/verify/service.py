import os
from typing import Optional


def verify_service(query: dict) -> Optional[str]:
    return (
        query.get("hub.challenge")
        if query.get("hub.mode") == "subscribe"
        and query.get("hub.verify_token") == os.getenv("WEBHOOK_TOKEN")
        else None
    )
