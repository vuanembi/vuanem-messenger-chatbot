import json

from messenger.component import template, converse
from messenger.postback.action import PostbackAction


def handler(messaging):
    payload_text = messaging["postback"]["payload"]

    try:
        payload = json.loads(payload_text)

        action = payload.get("action", "")

        if action == PostbackAction.PRODUCT_CATEGORY.value:
            handler = lambda messaging: converse(
                template.send_product_category,
                messaging,
            )
        elif action == PostbackAction.MATTRESS_CATEGORY.value:
            handler = lambda messaging: converse(
                template.send_mattress_category,
                messaging,
            )
        elif action == PostbackAction.STORE_LOCATION.value:
            handler = lambda messaging: converse(
                template.send_store_location,
                messaging,
            )
        elif action == PostbackAction.SUPPORT.value:
            handler = lambda messaging: converse(
                template.send_support,
                messaging,
            )
        else:
            handler = lambda _: True

        handler(messaging)

        return True

    except:
        return True
