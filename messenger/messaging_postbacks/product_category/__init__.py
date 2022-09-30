from messenger.repository import send_message_response
from messenger.component import template


def send_product_category(messaging):
    send_message_response(
        messaging["sender"]["id"],
        {"attachment": template.product_category_attachment()},
    )
