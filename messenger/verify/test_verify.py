import os

from messenger import verify


def test_verify_service():
    challenge = "123"
    query = {
        "hub.challenge": challenge,
        "hub.mode": "subscribe",
        "hub.verify_token": os.getenv("WEBHOOK_TOKEN"),
    }

    result = verify.verify_service(query)

    assert result == challenge
