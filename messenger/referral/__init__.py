from datetime import datetime

from db import bigquery


def handler(messaging):
    data = {
        "sender": {"id": messaging["sender"]["id"]},
        "recipient": {"id": messaging["recipient"]["id"]},
        "timestamp": datetime.utcfromtimestamp(messaging["timestamp"]).isoformat(),
        "referral": {
            "ref": messaging["referral"].get("ref"),
            "ad_id": messaging["referral"].get("ad_id"),
            "source": messaging["referral"].get("source"),
            "type": messaging["referral"].get("type"),
            "ads_context_data": {
                "ad_title": messaging["referral"]["ads_context_data"].get("ad_title"),
                "photo_url": messaging["referral"]["ads_context_data"].get("photo_url"),
                "video_url": messaging["referral"]["ads_context_data"].get("video_url"),
                "post_id": messaging["referral"]["ads_context_data"].get("post_id"),
                "product_id": messaging["referral"]["ads_context_data"].get(
                    "product_id"
                ),
            },
        },
    }

    bigquery.insert("p_MessagingReferrals", [data])

    return True
