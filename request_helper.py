import json

import requests


class RequestHelper:

    @staticmethod
    def get_match(match_id):
        cookies = {
            'dark-theme': '1',
            'sid': '5655600.G9LnnerUnPIAASQs4uW0stFCk9Yx%2FSzg2LB8qW72WYA',
            '_ym_uid': '1638982912395680522',
            '_ym_d': '1638982912',
            '_ga': 'GA1.2.1965141046.1638982914',
            'sidebarOpen': 'false',
            'so': 'false',
            'intercom-session-z5hvtvqq': 'Q3VpelhxM0ovY2RRZlFMR3QxT0gzK3lTTy8wNHlYWjhiZHhLbUFjOC9Fd1B4S2xUUDlJVVlBeG5zUUtSQkJ0UC0tZWRJQmRONnd4VTRtcGFrckFjcTNDQT09--218a8dffa8ad0e67163ed6670192c8d01c6cd5c1',
        }

        headers = {
            'authority': 'hasura.fastcup.net',
            'accept': '*/*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,kk;q=0.6',
            # Already added when you pass json=
            # 'content-type': 'application/json',
            # Requests sorts cookies= alphabetically
            # 'cookie': 'dark-theme=1; sid=5655600.G9LnnerUnPIAASQs4uW0stFCk9Yx%2FSzg2LB8qW72WYA; _ym_uid=1638982912395680522; _ym_d=1638982912; _ga=GA1.2.1965141046.1638982914; sidebarOpen=false; so=false; intercom-session-z5hvtvqq=Q3VpelhxM0ovY2RRZlFMR3QxT0gzK3lTTy8wNHlYWjhiZHhLbUFjOC9Fd1B4S2xUUDlJVVlBeG5zUUtSQkJ0UC0tZWRJQmRONnd4VTRtcGFrckFjcTNDQT09--218a8dffa8ad0e67163ed6670192c8d01c6cd5c1',
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

        json_data = {
            'operationName': 'GetMatchStats',
            'variables': {
                'gameID': 1,
                'id': 8098261,
            },
            'query': 'query GetMatchStats($id: Int!, $gameID: smallint!) {\n  match: matches_by_pk(id: $id) {\n    id\n    type\n    status\n    has_winner\n    cancellation_reason\n    started_at\n    finished_at\n    server_instance_id\n    best_of\n    max_rounds_count\n    maps(order_by: {number: asc}) {\n      id\n      number\n      game_status\n      started_at\n      finished_at\n      demo_url\n      demo_deleted\n      map {\n        id\n        name\n        raw_name\n        offset\n        flip_v\n        flip_h\n        scale\n        preview\n        topview\n        overview\n        __typename\n      }\n      __typename\n    }\n    game {\n      id\n      raw_name\n      __typename\n    }\n    gameMode {\n      id\n      team_size\n      __typename\n    }\n    teams(order_by: {id: asc}) {\n      id\n      captain_id\n      name\n      score\n      size\n      is_winner\n      initial_side\n      mapStats {\n        match_map_id\n        match_team_id\n        score\n        is_winner\n        initial_side\n        __typename\n      }\n      __typename\n    }\n    members {\n      private {\n        user {\n          ...UserCommon\n          ...UserStats\n          ...UserGeo\n          ...UserLastActiveBan\n          __typename\n        }\n        party_id\n        rating\n        __typename\n      }\n      role\n      match_team_id\n      rating_diff\n      connected\n      is_leaver\n      impact\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment UserCommon on users {\n  id\n  nickName: nick_name\n  avatar\n  online\n  isMobile: is_mobile\n  link\n  __typename\n}\n\nfragment UserStats on users {\n  stats(\n    where: {game_id: {_eq: $gameID}, map_id: {_is_null: true}, game_mode_id: {_is_null: false}}\n  ) {\n    gameModeID: game_mode_id\n    rating\n    place\n    kills\n    deaths\n    __typename\n  }\n  __typename\n}\n\nfragment UserGeo on users {\n  city {\n    id\n    regionID: region_id\n    name_ru\n    name_uk\n    name_en\n    name_de\n    name_pl\n    name_pt\n    name_es\n    name_hbs\n    name_tr\n    __typename\n  }\n  country {\n    id\n    name_ru\n    name_uk\n    name_en\n    name_de\n    name_pl\n    name_pt\n    name_es\n    name_hbs\n    name_tr\n    iso2\n    __typename\n  }\n  __typename\n}\n\nfragment UserLastActiveBan on users {\n  bans(\n    where: {active: {_eq: true}, game_id: {_eq: $gameID}}\n    order_by: {length_minutes: desc}\n    limit: 1\n  ) {\n    id\n    since\n    until\n    __typename\n  }\n  __typename\n}',
        }

        response = requests.post('https://hasura.fastcup.net/v1/graphql', headers=headers, cookies=cookies,
                                 json=json_data).json()
        return response

    @staticmethod
    def get_match_rounds(match_id):
        cookies = {
            'dark-theme': '1',
            'sid': '5655600.G9LnnerUnPIAASQs4uW0stFCk9Yx%2FSzg2LB8qW72WYA',
            '_ym_uid': '1638982912395680522',
            '_ym_d': '1638982912',
            '_ga': 'GA1.2.1965141046.1638982914',
            'sidebarOpen': 'false',
            'so': 'false',
            'intercom-session-z5hvtvqq': 'Q3VpelhxM0ovY2RRZlFMR3QxT0gzK3lTTy8wNHlYWjhiZHhLbUFjOC9Fd1B4S2xUUDlJVVlBeG5zUUtSQkJ0UC0tZWRJQmRONnd4VTRtcGFrckFjcTNDQT09--218a8dffa8ad0e67163ed6670192c8d01c6cd5c1',
        }

        headers = {
            'authority': 'hasura.fastcup.net',
            'accept': '*/*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,kk;q=0.6',
            # Already added when you pass json=
            # 'content-type': 'application/json',
            # Requests sorts cookies= alphabetically
            # 'cookie': 'dark-theme=1; sid=5655600.G9LnnerUnPIAASQs4uW0stFCk9Yx%2FSzg2LB8qW72WYA; _ym_uid=1638982912395680522; _ym_d=1638982912; _ga=GA1.2.1965141046.1638982914; sidebarOpen=false; so=false; intercom-session-z5hvtvqq=Q3VpelhxM0ovY2RRZlFMR3QxT0gzK3lTTy8wNHlYWjhiZHhLbUFjOC9Fd1B4S2xUUDlJVVlBeG5zUUtSQkJ0UC0tZWRJQmRONnd4VTRtcGFrckFjcTNDQT09--218a8dffa8ad0e67163ed6670192c8d01c6cd5c1',
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

        json_data = {
            'operationName': 'GetMatchRounds',
            'variables': {
                'matchID': 8098261,
                'matchMapID': None,
            },
            'query': 'query GetMatchRounds($matchID: Int!, $matchMapID: Int) {\n  match_rounds(\n    where: {match_id: {_eq: $matchID}, match_map_id: {_eq: $matchMapID}}\n    order_by: {id: asc}\n  ) {\n    id\n    started_at\n    finished_at\n    win_match_team_id\n    win_reason\n    events(order_by: {id: asc}) {\n      id\n      type\n      date\n      killer_id\n      victim_id\n      is_killer_bot\n      is_victim_bot\n      is_headshot\n      penetrated\n      assistant_id\n      weapon_id\n      __typename\n    }\n    __typename\n  }\n}',
        }

        response = requests.post('https://hasura.fastcup.net/v1/graphql', headers=headers, cookies=cookies,
                                 json=json_data)

    @staticmethod
    def get_match_member_stats():
        cookies = {
            'dark-theme': '1',
            'sid': '5655600.G9LnnerUnPIAASQs4uW0stFCk9Yx%2FSzg2LB8qW72WYA',
            '_ym_uid': '1638982912395680522',
            '_ym_d': '1638982912',
            '_ga': 'GA1.2.1965141046.1638982914',
            'sidebarOpen': 'false',
            'so': 'false',
            'intercom-session-z5hvtvqq': 'Q3VpelhxM0ovY2RRZlFMR3QxT0gzK3lTTy8wNHlYWjhiZHhLbUFjOC9Fd1B4S2xUUDlJVVlBeG5zUUtSQkJ0UC0tZWRJQmRONnd4VTRtcGFrckFjcTNDQT09--218a8dffa8ad0e67163ed6670192c8d01c6cd5c1',
        }

        headers = {
            'authority': 'hasura.fastcup.net',
            'accept': '*/*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,kk;q=0.6',
            # Already added when you pass json=
            # 'content-type': 'application/json',
            # Requests sorts cookies= alphabetically
            # 'cookie': 'dark-theme=1; sid=5655600.G9LnnerUnPIAASQs4uW0stFCk9Yx%2FSzg2LB8qW72WYA; _ym_uid=1638982912395680522; _ym_d=1638982912; _ga=GA1.2.1965141046.1638982914; sidebarOpen=false; so=false; intercom-session-z5hvtvqq=Q3VpelhxM0ovY2RRZlFMR3QxT0gzK3lTTy8wNHlYWjhiZHhLbUFjOC9Fd1B4S2xUUDlJVVlBeG5zUUtSQkJ0UC0tZWRJQmRONnd4VTRtcGFrckFjcTNDQT09--218a8dffa8ad0e67163ed6670192c8d01c6cd5c1',
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

        json_data = {
            'operationName': 'GetMatchMemberMapStats',
            'variables': {
                'matchID': 8098261,
            },
            'query': 'query GetMatchMemberMapStats($matchID: Int!) {\n  match_member_map_stats(where: {match_id: {_eq: $matchID}}) {\n    match_id\n    user_id\n    match_team_id\n    match_map_id\n    kills\n    deaths\n    assists\n    headshots\n    damage_avg\n    first_kills_tt\n    first_kills_ct\n    first_deaths_tt\n    first_deaths_ct\n    clutch_1v5\n    clutch_1v4\n    clutch_1v3\n    clutch_1v2\n    clutch_1v1\n    multikill_5k\n    multikill_4k\n    multikill_3k\n    multikill_2k\n    multikill_1k\n    airshots\n    oneshots\n    noscopes\n    wallbangs\n    __typename\n  }\n}',
        }

        response = requests.post('https://hasura.fastcup.net/v1/graphql', headers=headers, cookies=cookies,
                                 json=json_data)

    @staticmethod
    def get_match_weapon_stats():
        cookies = {
            'dark-theme': '1',
            'sid': '5655600.G9LnnerUnPIAASQs4uW0stFCk9Yx%2FSzg2LB8qW72WYA',
            '_ym_uid': '1638982912395680522',
            '_ym_d': '1638982912',
            '_ga': 'GA1.2.1965141046.1638982914',
            'sidebarOpen': 'false',
            'so': 'false',
            'intercom-session-z5hvtvqq': 'Q3VpelhxM0ovY2RRZlFMR3QxT0gzK3lTTy8wNHlYWjhiZHhLbUFjOC9Fd1B4S2xUUDlJVVlBeG5zUUtSQkJ0UC0tZWRJQmRONnd4VTRtcGFrckFjcTNDQT09--218a8dffa8ad0e67163ed6670192c8d01c6cd5c1',
        }

        headers = {
            'authority': 'hasura.fastcup.net',
            'accept': '*/*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,kk;q=0.6',
            # Already added when you pass json=
            # 'content-type': 'application/json',
            # Requests sorts cookies= alphabetically
            # 'cookie': 'dark-theme=1; sid=5655600.G9LnnerUnPIAASQs4uW0stFCk9Yx%2FSzg2LB8qW72WYA; _ym_uid=1638982912395680522; _ym_d=1638982912; _ga=GA1.2.1965141046.1638982914; sidebarOpen=false; so=false; intercom-session-z5hvtvqq=Q3VpelhxM0ovY2RRZlFMR3QxT0gzK3lTTy8wNHlYWjhiZHhLbUFjOC9Fd1B4S2xUUDlJVVlBeG5zUUtSQkJ0UC0tZWRJQmRONnd4VTRtcGFrckFjcTNDQT09--218a8dffa8ad0e67163ed6670192c8d01c6cd5c1',
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

        json_data = {
            'operationName': 'GetMatchWeaponsStats',
            'variables': {
                'matchID': 8098261,
            },
            'query': 'query GetMatchWeaponsStats($matchID: Int!) {\n  match_weapons_stats(where: {match_id: {_eq: $matchID}, hits: {_gt: 0}}) {\n    user_id\n    weapon_id\n    match_map_id\n    kills\n    headshots\n    damage_sum\n    hits\n    shots\n    __typename\n  }\n}',
        }

        response = requests.post('https://hasura.fastcup.net/v1/graphql', headers=headers, cookies=cookies,
                                 json=json_data)


class RequestMock:

    @staticmethod
    def get_match(match_id):
        with open('mock/mock_match.json', 'r') as mock:
            return json.load(mock)['data']['match']

    @staticmethod
    def get_match_rounds(match_id):
        with open('mock/match_rounds_mock.json', 'r') as mock:
            return json.load(mock)['data']['match_rounds']

    @staticmethod
    def get_match_member_stats(match_id):
        with open('mock/mock_match_member_stats.json', 'r') as mock:
            return json.load(mock)['data']['match_member_map_stats']

    @staticmethod
    def get_match_weapon_stats(match_id):
        with open('mock/match_weapons_stats.json', 'r') as mock:
            return json.load(mock)['data']['match_weapons_stats']
