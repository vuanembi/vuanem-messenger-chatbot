import httpx
import os


def _get_client() -> httpx.Client:
    return httpx.Client(
        base_url="https://graph.facebook.com/me/personas",
        params={
            "access_token": os.getenv('page_access_token')
        },
        timeout=None,
    )


def create_a_persona():
    todo = {
        "name": "Gấu Vua Nệm",
        "profile_picture_url": "https://scontent-hkt1-2.xx.fbcdn.net/v/t39.30808-6/245408297_4821319461234229_2151816139450913747_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=09cbfe&_nc_ohc=02l_i9zs_cUAX8kk3W9&_nc_ht=scontent-hkt1-2.xx&oh=00_AT-_ZPBtURbFxBx6r5Avirr3Ig9NQXY-dJqWyV4JW1vBIQ&oe=6329D0CB"
    }

    with _get_client() as client:
        r = client.request(
            'POST',
            "/",
            json=todo,
        )
        res = r.json()
        return res

