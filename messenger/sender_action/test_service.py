import os

from messenger.sender_action import service

def test_mark_seen():
    res = service.mark_seen(os.getenv('FB_PAGE_SCOPED_ID'))
    assert res

def test_typing_on():
    res = service.typing_on(os.getenv('FB_PAGE_SCOPED_ID'))
    assert res

def test_typing_off():
    res = service.typing_off(os.getenv('FB_PAGE_SCOPED_ID'))
    assert res