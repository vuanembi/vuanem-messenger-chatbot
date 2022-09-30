import json

from messenger.postback.action import PostbackAction

support_button = {
    "type": "postback",
    "title": "Tư vấn",
    "payload": json.dumps({"action": PostbackAction.SUPPORT.value}),
}
