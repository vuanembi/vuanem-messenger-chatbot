def mattress_category_carousel_attachment():
    return {
        "type": "template",
        "payload": {
            "template_type": "generic",
            "elements": [
                {
                    "title": "Đệm Foam",
                    "image_url": "https://i.imgur.com/hQZYNXA.png",
                    "subtitle": "Sale To Chào Tháng 10, Giảm Sốc Đến 50%++",
                    "default_action": {
                        "type": "web_url",
                        "url": "https://vuanem.com/nem/foam",
                    },
                },
                {
                    "title": "Đệm Cao Su",
                    "image_url": "https://i.imgur.com/HgxtI7e.png",
                    "subtitle": "Tặng kèm ưu đãi miễn phí giao hàng bảo hành chọn đời ",
                    "default_action": {
                        "type": "web_url",
                        "url": "https://vuanem.com/nem/cao-su",
                    },
                },
                {
                    "title": "Đệm Lò Xo",
                    "image_url": "https://i.imgur.com/afGTY49.png",
                    "subtitle": "Combo đệm lò xo kèm quà tặng cực ưu đãi!",
                    "default_action": {
                        "type": "web_url",
                        "url": "https://vuanem.com/nem/lo-xo",
                    },
                },
            ],
        },
    }
