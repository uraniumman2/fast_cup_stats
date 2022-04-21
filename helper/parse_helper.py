class ParseHelper:

    @staticmethod
    def parse_match(match):
        match_ = {'id': match['id'],
                  'started_at': match['started_at'],
                  'members': [{'user_id': member['private']['user']['id'], 'nickname': member['private']['user']['nickName']}
                              for member in
                              match['members']],
                  'maps': [{'id': map_['id'],
                            'name': map_['map']['name']} for map_ in match['maps']]}
        return match_

    @staticmethod
    def parse_match_member_stats(match_member_stats, map_id):
        match_member_stats_ = []
        for mms in match_member_stats:
            if mms['match_map_id'] == map_id:
                info = {'user_id': mms['user_id'],
                        'k': mms['kills'],
                        'd': mms['deaths'],
                        'adr': mms['damage_avg'],
                        'fk': mms['first_kills_tt'] + mms['first_kills_ct'],
                        'fd': mms['first_deaths_tt'] + mms['first_deaths_ct'],
                        '1v5': mms['clutch_1v5'],
                        '1v4': mms['clutch_1v4'],
                        '1v3': mms['clutch_1v3'],
                        '1v2': mms['clutch_1v2'],
                        '1v1': mms['clutch_1v1'],
                        'm5': mms['multikill_5k'],
                        'm4': mms['multikill_4k'],
                        'm3': mms['multikill_3k'],
                        'm2': mms['multikill_2k'],
                        'm1': mms['multikill_1k'],
                        }
                match_member_stats_.append(info)
        return match_member_stats_

    @staticmethod
    def parse_match_weapon_stats(match_weapon_stats, map_id):
        match_weapon_stats_ = []
        for mws in match_weapon_stats:
            if mws['match_map_id'] == map_id:
                info = {'user_id': mws['user_id'],
                        'weapon_id': mws['weapon_id'],
                        'match_map_id': mws['match_map_id'],
                        'kills': mws['kills'],
                        }
                match_weapon_stats_.append(info)
        return match_weapon_stats_
