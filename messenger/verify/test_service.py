import os

from messenger.verify.service import verify_service


def test_verify_service():
    challenge = "123"
    query = {
        "hub.challenge": challenge,
        "hub.mode": "subscribe",
        "hub.verify_token": os.getenv("WEBHOOK_TOKEN"),
    }

    result = verify_service(query)

    assert result == challenge
