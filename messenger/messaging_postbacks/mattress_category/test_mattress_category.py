from messenger.messaging_postbacks import mattress_category


def test_send_mattress_category():
    messaging = {"sender": {"id": "3707575876035255"}}

    res = mattress_category.send_mattress_category(messaging)
    assert res == None
