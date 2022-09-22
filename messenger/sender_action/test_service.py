import os

import pytest

from messenger.sender_action import service


@pytest.fixture()
def page_scoped_id():
    return os.getenv("FB_PAGE_SCOPED_ID")


@pytest.mark.parametrize(
    "action",
    [
        service.mark_seen,
        service.typing_on,
        service.typing_off,
    ],
    ids=["mark_seen", "typing_on", "typing_off"],
)
def test_sender_action_service(action):
    res = action(os.getenv("FB_PAGE_SCOPED_ID"))
    assert res
