from messenger.message_response.debug import service

messaging = {
    "sender": {"id": "3707575876035255"},
    "recipient": {"id": "153143011385254"},
    "timestamp": 1663563505357,
    "message": {"mid": "", "text": "ads"},
}


def test_send_message_response_service():
    res = service.debug_send_message_response(messaging)
    assert res == True


def test_echo():
    res = service.debug_echo(messaging)
    assert res == True
