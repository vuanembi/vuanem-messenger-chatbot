import os

import pytest

from messenger.component import sender_action


@pytest.fixture()
def page_scoped_id():
    return os.getenv("FB_PAGE_SCOPED_ID")


@pytest.mark.parametrize(
    "action",
    [
        sender_action.mark_seen,
        sender_action.typing_on,
        sender_action.typing_off,
    ],
    ids=["mark_seen", "typing_on", "typing_off"],
)
def test_sender_action_service(action):
    res = action({"sender": {"id": "3707575876035255"}})
    assert res
