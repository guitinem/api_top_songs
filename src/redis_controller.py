import json
from datetime import timedelta

import redis

r = redis.Redis(host="localhost", port=6379, db=0)


def save_artist_info(info: object):
    r.setex(info.get('artist_name'),
            timedelta(days=7),
            value=json.dumps(info)
            )

def get_artist_info(artist_name: str):
    response = r.get(artist_name)

    if not response:
        return None

    return json.loads(response)

def clean_cache():
    r.flushdb()
