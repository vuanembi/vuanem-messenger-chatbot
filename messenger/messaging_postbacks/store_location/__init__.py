from messenger.repository import send_message_response
from messenger.component import template


def send_store_location(messaging):
    send_message_response(
        messaging["sender"]["id"],
        {
            "text": "Vua Nệm gửi bạn Hệ thống Cửa hàng gần bạn nhất",
            "attachment": template.store_location_attachment(),
        },
    )
