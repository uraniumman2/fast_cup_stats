class Weapon:
    AWP = 5
    M4A1_S = 13
    M4A4 = 14
    AK47 = 3


class Role:
    SUPPORT = "supp"
    AWP = "awp"
    RIFFLE = "riffle"


class Request:
    HEADERS = {
        'authority': 'hasura.fastcup.net',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,kk;q=0.6',
        'origin': 'https://csgo.fastcup.net',
        'referer': 'https://csgo.fastcup.net/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
    }
