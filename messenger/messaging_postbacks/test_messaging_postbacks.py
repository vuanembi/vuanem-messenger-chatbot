import os
import json

import pytest

from messenger import messaging_postbacks


@pytest.mark.parametrize(
    "action",
    [
        messaging_postbacks.PostbackAction.MATTRESS_CATEGORY.value,
        messaging_postbacks.PostbackAction.PRODUCT_CATEGORY.value,
        messaging_postbacks.PostbackAction.STORE_LOCATION.value,
    ],
)
def test_messaging_postbacks(action):
    messaging = {
        "sender": {"id": os.getenv("FB_PAGE_SCOPED_ID")},
        "postback": {"payload": json.dumps({"action": action})},
    }

    res = messaging_postbacks.handler(messaging)

    assert res
