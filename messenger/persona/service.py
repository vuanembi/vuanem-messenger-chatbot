from typing import TypedDict

from messenger.repository import unversioned_client


class Persona(TypedDict):
    name: str
    profile_picture_url: str


def create_persona(persona: Persona):
    r = unversioned_client.post("me/personas", json=persona)
    return r.json()


def create_gau_vuanem_persona():
    persona = Persona(
        name="Gấu Vua Nệm",
        profile_picture_url="https://scontent-hkt1-2.xx.fbcdn.net/v/t39.30808-6/245408297_4821319461234229_2151816139450913747_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=09cbfe&_nc_ohc=02l_i9zs_cUAX8kk3W9&_nc_ht=scontent-hkt1-2.xx&oh=00_AT-_ZPBtURbFxBx6r5Avirr3Ig9NQXY-dJqWyV4JW1vBIQ&oe=6329D0CB",
    )
    return create_persona(persona)
