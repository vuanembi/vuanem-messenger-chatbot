from messenger.message import echo


messaging = {
    "sender": {"id": "3707575876035255"},
    "recipient": {"id": "153143011385254"},
    "timestamp": 1663563505357,
    "message": {"mid": "", "text": "ads"},
}


def test_echo():
    res = echo.echo_service(messaging)
    assert res == True
