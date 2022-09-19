import json
import httpx
import os


def _get_client() -> httpx.Client:
    return httpx.Client(
        base_url="https://graph.facebook.com/v14.0/me/messages",
        params={
            "access_token": os.getenv('page_access_token')
        },
        timeout=None,
    )


def mark_seen(recipient_id: str) -> dict:
    headers = {"Content-Type": "application/json"}
    todo = {
        "messaging_type": "RESPONSE",
        "recipient": {
            "id": recipient_id
        },
        "sender_action": "mark_seen"
    }

    with _get_client() as client:
        r = client.request(
            'POST',
            "/",
            json=todo,
            headers=headers,
        )
        res = r.json()
        return res
