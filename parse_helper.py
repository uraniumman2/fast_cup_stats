class ParseHelper:

    @staticmethod
    def parse_match(match):
        match_ = {'id': match['id'],
                  'members': [{'id': member['private']['user']['id'], 'nickname': member['private']['user']['nickName']}
                              for member in
                              match['members']]}
        return match_

    @staticmethod
    def parse_match_member_stats(match_member_stats):
        match_member_stats_ = []
        for mms in match_member_stats:
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
