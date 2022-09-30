from messenger.repository import send_message_response
from messenger.component.template import attachments


def send_mattress_category(messaging):
    send_message_response(
        messaging["sender"]["id"],
        {"attachment": attachments.mattress_category_attachment()},
    )


def send_product_category(messaging):
    send_message_response(
        messaging["sender"]["id"],
        {"attachment": attachments.product_category_attachment()},
    )


def send_store_location(messaging):
    send_message_response(
        messaging["sender"]["id"],
        {"attachment": attachments.store_location_attachment()},
    )
