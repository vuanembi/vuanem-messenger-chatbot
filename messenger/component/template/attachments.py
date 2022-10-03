from messenger.component.template import button


def product_category_attachment():
    return {
        "type": "template",
        "payload": {
            "template_type": "generic",
            "elements": [
                {
                    "title": "Nệm",
                    "image_url": "https://i.imgur.com/Xss0WL8.png",
                    "subtitle": "Nệm chất lượng tốt nhất thị trường, cho giấc ngủ sâu, êm ái cho gia đình thân yêu",
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
                    "title": "Chăn Ga",
                    "image_url": "https://i.imgur.com/aqieJYW.png",
                    "subtitle": "Mẫu mã phong phú, đa dạng, chất lượng cao cấp, giao hàng nhanh chóng",
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
                    "image_url": "https://i.imgur.com/74F5Epl.png",
                    "subtitle": "Bảo vệ nệm đa năng, gối chống đau cổ vai gáy, tấm tăng diện tích đệm",
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
                    "image_url": "https://i.imgur.com/YossddM.png",
                    "subtitle": "Thiết kế hiện đại, sang trọng, tích hợp các tính năng thông minh, giá tốt, giảm đến 40%",
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
                    "title": "Nệm lò xo",
                    "image_url": "https://i.imgur.com/luPnoRa.png",
                    "subtitle": "Nệm lò xo túi độc lập cao cấp, chống rung vượt trội, thiết kế sang trọng, an toàn sức khỏe",
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
                    "title": "Nệm Foam - Cao su non",
                    "image_url": "https://i.imgur.com/ruTugF6.png",
                    "subtitle": "Êm ái và nâng đỡ tốt, siêu mềm nhẹ, tính cơ động cao, thích hợp cho mọi gia đình",
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
                    "title": "Nệm Cao Su",
                    "image_url": "https://i.imgur.com/7pRMjKu.png",
                    "subtitle": "Cao su 100% tự nhiên, thông thoáng tuyệt đối, tránh đau lưng khi ngủ",
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
                    "title": "Nệm bông ép",
                    "image_url": "https://i.imgur.com/pOeznpd.png",
                    "subtitle": "Nệm bông ép giá rẻ, bền chắc, ổn định và thông thoáng, gấp 3 linh hoạt",
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
                    "image_url": "https://i.imgur.com/ZhTckht.png",
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
