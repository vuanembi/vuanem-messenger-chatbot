import os

from messenger.component.template import (
    send_mattress_category,
    send_product_category,
    send_store_location,
    send_support,
)

sender_id = os.getenv("FB_PAGE_SCOPED_ID")


def test_send_product_category():
    messaging = {"sender": {"id": sender_id}}

    res = send_product_category(messaging)
    assert res == None


def test_send_mattress_category():
    messaging = {"sender": {"id": sender_id}}

    res = send_mattress_category(messaging)
    assert res == None


def test_send_store_location():
    messaging = {"sender": {"id": sender_id}}

    res = send_store_location(messaging)
    assert res == None


def test_send_support():
    messaging = {"sender": {"id": sender_id}}

    res = send_support(messaging)
    assert res == None
