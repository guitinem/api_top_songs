from requests import get

URL_BASE = "https://api.genius.com/"
TOKEN = "JuR2WR4AGw0S5eE_6HxVPNDufQrJeCbUvfnJl13Xy7xFmbkWED4wlxIxDswkIEsf"


def search_artist_id(artist: str):

    payload = {
        'q': artist
    }

    headers = {
        'Authorization': f'Bearer {TOKEN}'
    }

    response = get(URL_BASE + 'search', params=payload, headers=headers)

    if (response.status_code != 200):
        return False

    data = response.json()

    try:
        artist_id = data['response']['hits'][0].get(
            'result').get('primary_artist').get('id')
    except:
        artist_id = None

    return artist_id


def search_top_songs(artist_id: int):

    headers = {
        'Authorization': f'Bearer {TOKEN}'
    }

    payload = {
        'sort': 'popularity',
        'per_page': '10'
    }

    url = f'{URL_BASE}artists/{artist_id}/songs'
    
    response = get(url, params=payload, headers=headers)

    if (response.status_code != 200):
        return None

    data = response.json()

    try:
        list_songs = [song.get('full_title')
                      for song in data['response']['songs']]
    except Exception as e:
        print(e)
        return None

    return list_songs
