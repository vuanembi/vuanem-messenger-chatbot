from datetime import datetime

from messenger import referral


def test_message_referral_handler():
    messaging = {
        "sender": {"id": "1254459154682919"},
        "recipient": {"id": "682498171943165"},
        "timestamp": int(datetime.utcnow().timestamp()),
        "referral": {
            "ref": "ref",
            "ad_id": "11111",
            "source": "ADS",
            "type": "OPEN_THREAD",
            "ads_context_data": {
                "ad_title": "ad_title",
                "photo_url": "photo_url",
                "video_url": "video_url",
                "post_id": "11111",
                "product_id": "11111",
            },
        },
    }

    res = referral.handler(messaging)

    assert not res
