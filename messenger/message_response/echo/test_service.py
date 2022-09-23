from messenger.message_response.echo import service


messaging = {
    "sender": {"id": "3707575876035255"},
    "recipient": {"id": "153143011385254"},
    "timestamp": 1663563505357,
    "message": {"mid": "", "text": "ads"},
}

def test_echo():
    res = service.echo(messaging)
    assert res == True
