from messenger.component.template import (
    send_mattress_category,
    send_product_category,
    send_store_location,
)


def test_send_mattress_category():
    messaging = {"sender": {"id": "3707575876035255"}}

    res = send_mattress_category(messaging)
    assert res == None


def test_send_product_category():
    messaging = {"sender": {"id": "3707575876035255"}}

    res = send_product_category(messaging)
    assert res == None


def test_send_store_location():
    messaging = {"sender": {"id": "3707575876035255"}}

    res = send_store_location(messaging)
    assert res == None
