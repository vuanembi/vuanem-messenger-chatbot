from messenger.message import debug

messaging = {
    "sender": {"id": "3707575876035255"},
    "recipient": {"id": "153143011385254"},
    "timestamp": 1663563505357,
    "message": {"mid": "", "text": "ads"},
}


def test_debug_send_message_response_service():
    res = debug.debug_service(messaging)
    assert res == True
