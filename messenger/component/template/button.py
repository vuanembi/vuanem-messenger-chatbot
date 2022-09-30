import json

from messenger.messaging_postbacks.postbacks import PostbackAction

support_button = {
    "type": "postback",
    "title": "Tư vấn",
    "url": json.dumps({"action": PostbackAction.SUPPORT.value}),
}
