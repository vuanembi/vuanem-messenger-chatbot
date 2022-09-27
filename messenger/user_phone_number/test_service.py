from messenger.user_phone_number.service import check_phone_number, get_sender_id, timestamp_to_datetime, controller

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


def test_get_phone_number():
    phone_number = check_phone_number(messaging)
    assert True


def test_get_sender_id():
    sender_id = get_sender_id(messaging)
    assert sender_id == "1254459154682919"


def test_timestamp_to_datetime():
    ts = timestamp_to_datetime(messaging)
    assert ts == "2017-08-16T17:52:56"


def test_controller():
    rows = controller(messaging)
    assert True
