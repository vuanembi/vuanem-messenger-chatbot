import re
from datetime import datetime
from db.bigquery import load

schema = [
    {
        "name": "sender_id",
        "type": "STRING"
    },
    {
        "name": "phone_number",
        "type": "STRING"
    },
    {
        "name": "created_date",
        "type": "TIMESTAMP"
    }
]


def get_sender_id(messaging) -> str:
    return messaging["sender"]["id"]


def get_phone_number(messaging) -> str:
    rgx_phone = re.compile(r"^\+84[0-9]{3,14}$")
    payload = messaging["message"]["quick_reply"]["payload"]

    if re.findall(rgx_phone, payload):
        return payload
    else:
        return None


def timestamp_to_datetime(messaging):
    ts = messaging["timestamp"]
    return datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')


def parse_data(messaging) -> list[dict]:
    return [
        {
            'sender_id': get_sender_id(messaging),
            'phone_number': get_phone_number(messaging),
            'created_date': timestamp_to_datetime(messaging)
        }
    ]


def controller(messaging):
    rows = parse_data(messaging)
    res = load('QuickReplies__PhoneNumber', schema=schema,
               id_key='created_date', cursor_key=None, rows=rows)
    return res
