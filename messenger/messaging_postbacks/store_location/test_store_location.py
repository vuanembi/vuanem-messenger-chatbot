from messenger.messaging_postbacks import store_location


def test_send_store_location():
    messaging = {"sender": {"id": "3707575876035255"}}

    res = store_location.send_store_location(messaging)
    assert res == None
