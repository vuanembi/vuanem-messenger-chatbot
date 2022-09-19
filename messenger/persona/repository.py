from typing import TypedDict

from messenger.repository import unversioned_client


class Persona(TypedDict):
    name: str
    profile_picture_url: str


def create_persona(persona: Persona):
    r = unversioned_client.post("me/personas", json=persona)
    return r.json()
