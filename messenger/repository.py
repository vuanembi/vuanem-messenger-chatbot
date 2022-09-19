import os

import httpx

client = httpx.Client(
    base_url="https://graph.facebook.com/v14.0",
    params={"access_token": os.getenv("PAGE_ACCESS_TOKEN", "")},
)
