from messenger.sender_action.repository import send_sender_action
mark_seen = send_sender_action("mark_seen")
typing_on = send_sender_action("typing_on")
typing_off = send_sender_action("typing_off")
