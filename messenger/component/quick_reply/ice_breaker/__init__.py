from messenger.component.template import (
    send_product_category,
    send_mattress_category,
    send_store_location,
    send_support,
)


def handler(messaging):
    payload: str = (
        messaging.get("message", {}).get("quick_reply", {}).get("payload", "")
    )

    if payload == "custom_question_0":
        send_product_category(messaging)
    elif payload == "custom_question_1":
        send_mattress_category(messaging)
    elif payload == "custom_question_2":
        send_store_location(messaging)
    elif payload == "custom_question_3":
        send_support(messaging)

    return True
