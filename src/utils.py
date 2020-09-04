import re

def get_artist_name(name_artist: str):
    """Return the name of the artist formtaed

    Args:
        name_artist (str)

    Returns:
        str: name of the artist
    """
    result_regex = re.findall('[a-zA-Z0-9]', name_artist)
    result_regex = ''.join(result_regex)

    return result_regex.lower()
