import os
import json

import pytest

from messenger import postback


@pytest.mark.parametrize(
    "action",
    [
        postback.PostbackAction.MATTRESS_CATEGORY.value,
        postback.PostbackAction.PRODUCT_CATEGORY.value,
        postback.PostbackAction.STORE_LOCATION.value,
        postback.PostbackAction.SUPPORT.value,
    ],
)
def test_messaging_postbacks(action):
    messaging = {
        "sender": {"id": os.getenv("FB_PAGE_SCOPED_ID")},
        "postback": {"payload": json.dumps({"action": action})},
    }

    res = postback.handler(messaging)

    assert res
