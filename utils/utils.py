import re


def get_match_id(url):
    match_id = re.search(r'(?<=https://csgo\.fastcup\.net/match)\d*', url)
    return match_id[0] if match_id else None
