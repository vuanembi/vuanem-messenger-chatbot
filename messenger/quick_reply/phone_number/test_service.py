from datetime import datetime

from messenger.quick_reply.phone_number.service import handler


def test_quick_reply_phone_number_handler_success():
    messaging = {
        "sender": {"id": "1254459154682919"},
        "recipient": {"id": "682498171943165"},
        "timestamp": int(datetime.utcnow().timestamp()),
        "message": {
            "quick_reply": {"payload": "+84773314403"},
            "mid": "m_AG5Hz2Uq7tuwNEhXfYYKj8mJEM_QPpz5jdCK48PnKAjSdjfipqxqMvK8ma6AC8fplwlqLP_5cgXIbu7I3rBN0P",
            "text": "+84773314403",
        },
    }

    res = handler(messaging)

    assert not res


def test_quick_reply_phone_number_handler_skip():
    messaging = {
        "sender": {"id": "1254459154682919"},
        "recipient": {"id": "682498171943165"},
        "timestamp": int(datetime.utcnow().timestamp()),
        "message": {
            "mid": "m_AG5Hz2Uq7tuwNEhXfYYKj8mJEM_QPpz5jdCK48PnKAjSdjfipqxqMvK8ma6AC8fplwlqLP_5cgXIbu7I3rBN0P",
            "text": "+84773314403",
        },
    }

    res = handler(messaging)

    assert res == None
