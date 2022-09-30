import re
from datetime import datetime

from db import bigquery


def add():
    return {"content_type": "user_phone_number"}


def handler(messaging):
    phone_pattern = re.compile(r"^\+84[0-9]{3,14}$")

    payload: str = (
        messaging.get("message", {}).get("quick_reply", {}).get("payload", "")
    )

    matched_payload = re.search(phone_pattern, payload)

    if matched_payload:
        data = {
            "sender": {"id": messaging["sender"]["id"]},
            "recipient": {"id": messaging["recipient"]["id"]},
            "mid": messaging["message"]["mid"],
            "phone_number": matched_payload.string,
            "timestamp": datetime.utcfromtimestamp(
                messaging["timestamp"] / 1000
            ).isoformat(),
        }

        return bigquery.insert("p_QuickReply__PhoneNumber", [data])
    else:
        return None
