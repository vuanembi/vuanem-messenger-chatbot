from messenger.user_phone_number.service import controller

messaging = {
    "sender": {
        "id": "1254459154682919"
    },
    "recipient": {
        "id": "682498171943165"
    },
    "timestamp": 1502905976,
    "message": {
        "quick_reply": {
            "payload": "+84773314403"
        },
        "mid": "m_AG5Hz2Uq7tuwNEhXfYYKj8mJEM_QPpz5jdCK48PnKAjSdjfipqxqMvK8ma6AC8fplwlqLP_5cgXIbu7I3rBN0P",
        "text": "+84773314403"
    }
}


def test_controller():
    rows = controller(messaging)
    assert True
