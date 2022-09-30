from typing import Callable

from messenger.component import sender_action


def converse(handler: Callable, messaging):
    sender_action.mark_seen(messaging)
    sender_action.typing_on(messaging)
    handler(messaging)
    sender_action.typing_off(messaging)
