import os

import httpx

BASE_URL = "https://graph.facebook.com"


def create_client(base_url: str):
    return httpx.Client(
        base_url=base_url,
        headers={"Content-Type": "application/json"},
        params={"access_token": os.getenv("FB_PAGE_ACCESS_TOKEN", "")},
    )


client = create_client(f"{BASE_URL}/v14.0")

unversioned_client = create_client(f"{BASE_URL}")


def send_message(recipient_id: str, payload: dict) -> dict:
    payload = {
        "recipient": {"id": recipient_id},
        **payload,
    }

    r = client.post("me/messages", json=payload)
    data = r.json()

    if r.status_code == 200:
        return data
    else:
        print(data)
        return data


def send_message_response(recipient_id: str, message: dict) -> dict:
    payload = {
        "messaging_type": "RESPONSE",
        "message": message,
    }
    return send_message(recipient_id, payload)
