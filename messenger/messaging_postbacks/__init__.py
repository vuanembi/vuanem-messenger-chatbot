import json

from messenger.messaging_postbacks import (
    product_category,
    mattress_category,
    store_location,
)


def handler(messaging):
    payload_text = messaging["postback"]["payload"]

    try:
        payload = json.loads(payload_text)

        action = payload.get("action", "")

        if action == "PRODUCT_CATEGORY":
            handler = product_category.send_product_category
        elif action == "MATTRESS_CATEGORY":
            handler = mattress_category.send_mattress_category
        elif action == "STORE_LOCATION":
            handler = store_location.send_store_location
        else:
            handler = lambda _: True

        handler(messaging)

        return True
    except:
        return True
