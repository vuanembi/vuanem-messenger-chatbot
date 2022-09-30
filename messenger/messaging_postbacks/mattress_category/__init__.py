from messenger.repository import send_message_response
from messenger.component import template


def send_mattress_category(messaging):
    send_message_response(
        messaging["sender"]["id"],
        {
            "text": "Vua Nệm gửi bạn danh sách các sản phẩm Nệm - Đệm",
            "attachment": template.mattress_category_attachment(),
        },
    )
