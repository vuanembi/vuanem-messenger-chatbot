import re
from datetime import datetime
from db.bigquery import client

DATASET = "IP_Messenger"


def insert(table, rows) -> int:
    output_rows = (
        client.insert_rows_json(
            f"{DATASET}.{table}", rows,
        )
    )
    return output_rows


def get_sender_id(messaging) -> str:
    return messaging["sender"]["id"]


def check_phone_number(messaging) -> str:
    rgx_phone = re.compile(r"^\+84[0-9]{3,14}$")
    payload = messaging["message"]["quick_reply"]["payload"]

    if re.findall(rgx_phone, payload):
        return True
    else:
        return False


def timestamp_to_datetime(messaging):
    ts = messaging["timestamp"]
    return datetime.utcfromtimestamp(ts).isoformat()


def parse_data(messaging) -> list[dict]:
    if check_phone_number(messaging):
        return [
            {
                'sender_id': get_sender_id(messaging),
                'phone_number': messaging["message"]["quick_reply"]["payload"],
                'created_at': timestamp_to_datetime(messaging)
            }
        ]
    else:
        return None


def controller(messaging):
    rows = parse_data(messaging)
    res = insert('QuickReplies__PhoneNumber', rows=rows)
    return res
