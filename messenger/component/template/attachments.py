from messenger.component.template import button


def product_category_attachment():
    return {
        "type": "template",
        "payload": {
            "template_type": "generic",
            "elements": [
                {
                    "title": "Nệm - Đệm",
                    "image_url": "https://i.imgur.com/hQZYNXA.png",
                    "subtitle": "Mua Nệm, Đệm giá tốt đến ngay Vua Nệm",
                    "default_action": {
                        "type": "web_url",
                        "url": "https://vuanem.com/nem",
                    },
                    "buttons": [
                        {
                            "type": "web_url",
                            "url": "https://vuanem.com/nem",
                            "title": "Tham khảo",
                        },
                        button.support_button,
                    ],
                },
                {
                    "title": "Chăn Ga Gối - Drap Giường",
                    "image_url": "https://i.imgur.com/HgxtI7e.png",
                    "subtitle": "Chăn Ga Gối Nệm Chính Hãng Cao Cấp",
                    "default_action": {
                        "type": "web_url",
                        "url": "https://vuanem.com/chan-ga-goi",
                    },
                    "buttons": [
                        {
                            "type": "web_url",
                            "url": "https://vuanem.com/chan-ga-goi",
                            "title": "Tham khảo",
                        },
                        button.support_button,
                    ],
                },
                {
                    "title": "Phụ Kiện",
                    "image_url": "https://i.imgur.com/afGTY49.png",
                    "subtitle": "Phụ kiện cao cấp nhập khẩu chính hãng",
                    "default_action": {
                        "type": "web_url",
                        "url": "https://vuanem.com/phu-kien",
                    },
                    "buttons": [
                        {
                            "type": "web_url",
                            "url": "https://vuanem.com/phu-kien",
                            "title": "Tham khảo",
                        },
                        button.support_button,
                    ],
                },
                {
                    "title": "Giường",
                    "image_url": "https://i.imgur.com/hQZYNXA.png",
                    "subtitle": "Mua giường ngủ giá rẻ, cao cấp tại Vua Nệm",
                    "default_action": {
                        "type": "web_url",
                        "url": "https://vuanem.com/giuong",
                    },
                    "buttons": [
                        {
                            "type": "web_url",
                            "url": "https://vuanem.com/giuong",
                            "title": "Tham khảo",
                        },
                        button.support_button,
                    ],
                },
            ],
        },
    }


def mattress_category_attachment():
    return {
        "type": "template",
        "payload": {
            "template_type": "generic",
            "elements": [
                {
                    "title": "Foam - Cao su non",
                    "image_url": "https://i.imgur.com/hQZYNXA.png",
                    "subtitle": "Sale To Chào Tháng 10, Giảm Sốc Đến 50%++",
                    "default_action": {
                        "type": "web_url",
                        "url": "https://vuanem.com/nem/foam",
                    },
                    "buttons": [
                        {
                            "type": "web_url",
                            "url": "https://vuanem.com/nem/foam",
                            "title": "Tham khảo",
                        },
                        button.support_button,
                    ],
                },
                {
                    "title": "Cao Su",
                    "image_url": "https://i.imgur.com/HgxtI7e.png",
                    "subtitle": "Tặng kèm ưu đãi miễn phí giao hàng bảo hành chọn đời ",
                    "default_action": {
                        "type": "web_url",
                        "url": "https://vuanem.com/nem/cao-su",
                    },
                    "buttons": [
                        {
                            "type": "web_url",
                            "url": "https://vuanem.com/nem/cao-su",
                            "title": "Tham khảo",
                        },
                        button.support_button,
                    ],
                },
                {
                    "title": "Lò Xo",
                    "image_url": "https://i.imgur.com/afGTY49.png",
                    "subtitle": "Combo đệm lò xo kèm quà tặng cực ưu đãi!",
                    "default_action": {
                        "type": "web_url",
                        "url": "https://vuanem.com/nem/cao-su",
                    },
                    "buttons": [
                        {
                            "type": "web_url",
                            "url": "https://vuanem.com/nem/cao-su",
                            "title": "Tham khảo",
                        },
                        button.support_button,
                    ],
                },
            ],
        },
    }


def store_location_attachment():
    return {
        "type": "template",
        "payload": {
            "template_type": "generic",
            "elements": [
                {
                    "title": "Hệ thống Cửa hàng",
                    "image_url": "https://i.imgur.com/hQZYNXA.png",
                    "subtitle": "Hệ thống 152 cửa hàng Chăn ga Gối Nệm",
                    "default_action": {
                        "type": "web_url",
                        "url": "https://vuanem.com/stores",
                    },
                    "buttons": [
                        {
                            "type": "web_url",
                            "url": "https://vuanem.com/stores",
                            "title": "Tham khảo",
                        },
                        button.support_button,
                    ],
                },
            ],
        },
    }
