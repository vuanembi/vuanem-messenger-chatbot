from messenger.repository import send_message_response
from messenger.component import template


def send_product_category(messaging):
    send_message_response(
        messaging["sender"]["id"],
        {
            "text": "Vua Nệm gửi bạn danh sách sản phẩm",
            "attachment": template.product_category_attachment(),
        },
    )
