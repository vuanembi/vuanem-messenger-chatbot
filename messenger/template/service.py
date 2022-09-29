from messenger.repository import client


def create_template_generic(recipient_id: str) -> dict:
    jsonload = {
        "recipient": {"id": recipient_id},
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                        {
                            "title": "Đệm Foam",
                            "image_url": "https://scontent-hkt1-2.xx.fbcdn.net/v/t39.30808-6/279766791_5477038505662318_2784517453825327357_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=730e14&_nc_ohc=AdbLOAb4kSYAX9eW34O&_nc_ht=scontent-hkt1-2.xx&oh=00_AT-UloPV49a24k8lq2krni3GqumB-lNjQbA47dPix4oZ-Q&oe=633AED92",
                            "subtitle": "Sale To Chào Tháng 10, Giảm Sốc Đến 50%++"
                        },
                        {
                            "title": "Đệm Cao Su",
                            "image_url": "https://scontent-hkt1-2.xx.fbcdn.net/v/t39.30808-6/304937096_2887149621429121_5781232094763100297_n.jpg?_nc_cat=105&ccb=1-7&_nc_sid=730e14&_nc_ohc=2xWfYOFH0YwAX9tUaZt&_nc_ht=scontent-hkt1-2.xx&oh=00_AT_cDD32jYcJ8ZNbaq-L4L5RT9TxUxe_k8-M_O2HaJ4Lmg&oe=6339D5B5",
                            "subtitle": "Tặng kèm ưu đãi miễn phí giao hàng bảo hành chọn đời "
                        },
                        {
                            "title": "Đệm Lò Xo",
                            "image_url": "https://scontent-hkt1-1.xx.fbcdn.net/v/t1.6435-9/52590289_1609859912491438_9012976432430710784_n.jpg?_nc_cat=111&ccb=1-7&_nc_sid=730e14&_nc_ohc=oTT9DFwjCgkAX8nXjaz&_nc_ht=scontent-hkt1-1.xx&oh=00_AT-GcQ-vOjC55RDZT_KXQz-B04doDLVuiw5R1JVhEjnFAg&oe=635AD783",
                            "subtitle": "Combo đệm lò xo kèm quà tặng cực ưu đãi!"
                        }
                    ]
                }
            }
        }
    }

    r = client.post("me/messages", json=jsonload)
    data = r.json()

    if r.status_code == 200:
        return data
    else:
        print(data)
        return data
