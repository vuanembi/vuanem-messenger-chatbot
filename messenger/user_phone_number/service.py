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


def quick_reply_phone_number_capture(messaging):
    rgx_phone = re.compile(r"^\+84[0-9]{3,14}$")
    payload = messaging["message"]["quick_reply"]["payload"]

    if re.findall(rgx_phone, payload):
        return [
            {
                'sender_id': messaging["sender"]["id"],
                'phone_number': messaging["message"]["quick_reply"]["payload"],
                'created_at': datetime.utcfromtimestamp(messaging["timestamp"]).isoformat()
            }
        ]
    else:
        return None


def controller(messaging):
    rows =quick_reply_phone_number_capture(messaging)
    res = insert('QuickReplies__PhoneNumber', rows=rows)
    return res
