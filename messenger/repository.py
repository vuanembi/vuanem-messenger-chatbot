import os

import httpx

BASE_URL = "https://graph.facebook.com"

client = httpx.Client(
    base_url=f"{BASE_URL}/v14.0",
    params={"access_token": os.getenv("FB_PAGE_ACCESS_TOKEN", "")},
)

unversioned_client = httpx.Client(
    base_url=BASE_URL,
    params={"access_token": os.getenv("FB_PAGE_ACCESS_TOKEN", "")},
)
