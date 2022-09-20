import os

from messenger.sender_action import service

def test_typing_on():
    res = service.mark_seen(os.getenv('FB_PAGE_SCOPED_ID'))
    assert res
