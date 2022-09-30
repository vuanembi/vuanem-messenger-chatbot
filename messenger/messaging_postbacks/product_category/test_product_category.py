from messenger.messaging_postbacks import product_category


def test_send_product_category():
    messaging = {"sender": {"id": "3707575876035255"}}

    res = product_category.send_product_category(messaging)
    assert res == None
