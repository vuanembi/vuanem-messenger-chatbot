import re
from google.cloud import bigquery
import numpy as np
from datetime import datetime

client = bigquery.Client()


def parse_data(messaging) -> dict:
    return
    [
        {
            'sender': {id: messaging["sender"].get("id")}
            if (messaging["sender"].get("id")) else {},
            'recipient': {id: messaging["recipient"].get("id")}
            if (messaging["recipient"].get("id")) else {},
            'created_date': {datetime.utcfromtimestamp(messaging["timestamp"]).isoformat()},
            'referral':{
                "ref": messaging["referral"].get("ref")
                if (messaging["referral"].get("ref")) else {},

                "ad_id": messaging["referral"].get("ad_id")
                if (messaging["referral"].get("ad_id")) else {},

                source: messaging["referral"].get("source")
                if (messaging["referral"].get("source")) else {},

                "type": messaging["referral"].get("type")
                if (messaging["referral"].get("type")) else {},

                "ad_tittle": messaging["referral"]["ads_context_data"].get("ad_tittle")
                if (messaging["referral"]["ads_context_data"].get("ad_tittle")) else {},

                "photo_url": messaging["referral"]["ads_context_data"].get("photo_url")
                if (messaging["referral"]["ads_context_data"].get("photo_url")) else {},

                "video_url": messaging["referral"]["ads_context_data"].get("video_ul")
                if (messaging["referral"]["ads_context_data"].get("video_ul")) else {},

                "post_id": messaging["referral"]["ads_context_data"].get("post_id")
                if (messaging["referral"]["ads_context_data"].get("post_id")) else {},

                "product_id": messaging["referral"]["ads_context_data"].get("product_id")
                if (messaging["referral"]["ads_context_data"].get("product_id")) else {},
            }
        }
    ]


def insert(rows):
    client.insert_rows_json(
        "IP_Messenger.MessagingReferrals", rows
    )


def messaging_referrals(messaging):
    rows = parse_data(messaging)
    res = insert(rows=rows)
