from messenger.message_response.debug import service


def test_debug_service():
    messaging = {
        "sender": {"id": "3707575876035255"},
        "recipient": {"id": "153143011385254"},
        "timestamp": 1663563505357,
        "message": {
            "mid": "m_tShq36qYjA8tRXpBE8Mi4BtO3DMoAfweFY82MmuyfeFy8vvDJzHanLjUwo6YGlKgwpC8uQQjb2HM_kVxyRtxSg",
            "text": "ads",
        },
    }
    res = service.debug(messaging)
    assert res == True
