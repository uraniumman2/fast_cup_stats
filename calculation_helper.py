from static import Weapon


class CalculationHelper:

    @staticmethod
    def calculate_score():
        pass

    @staticmethod
    def calculate_basic_score(match_member_stats):
        match_member_stats_ = []
        for mms in match_member_stats:
            kd = mms['k'] / mms['d'] if mms['d'] != 0 else 0
            adr = mms['adr']
            fk = mms['fk'] * (1 - 1 / mms['k']) if mms['k'] != 0 else 0
            fd = mms['fd'] * (1 - 1 / mms['d']) if mms['d'] != 0 else 0
            v5, v4, v3, v2, v1 = mms['1v5'], mms['1v4'], mms['1v3'], mms['1v2'], mms['1v1']
            m5, m4, m3, m2, m1 = mms['m5'], mms['m4'], mms['m3'], mms['m2'], mms['m1']
            clutch_rate = v5 * 0.1 + v4 * 0.08 + v3 * 0.06 + v2 * 0.04 + v1 * 0.02
            # TODO: if sup clutch_rate * 1.2
            multi_kill = m5 * 0.05 + m4 * 0.04 + m3 * 0.03 + m2 * 0.02 + m1 * 0.01
            basic = kd * 0.2 + adr * 0.2 + fk + fd + clutch_rate + multi_kill

            info = {
                'user_id': mms['user_id'],
                'basic': basic,
            }
            match_member_stats_.append(info)
        return match_member_stats_

    @staticmethod
    def calculate_weapon_score(match_member_stats, weapon_stats):
        match_member_stats_ = []
        for mms in match_member_stats:
            user_id = mms['user_id']
            kills = mms['k']
            awp = CalculationHelper.get_weapon_kills_(user_id=user_id,
                                                      weapon_stats=weapon_stats,
                                                      weapon_ids=[Weapon.AWP])
            riffle = CalculationHelper.get_weapon_kills_(user_id=user_id,
                                                         weapon_stats=weapon_stats,
                                                         weapon_ids=[Weapon.AK47, Weapon.M4A4, Weapon.M4A1_S])
            supp = 0
            info = {
                'user_id': user_id,
                'awp': awp / (kills * 2) if kills != 0 else 0,
                'riffle': riffle / (kills * 3) if kills != 0 else 0,
                'supp': supp,
            }
            match_member_stats_.append(info)
        return match_member_stats_

    @staticmethod
    def get_weapon_kills_(user_id, weapon_stats, weapon_ids):
        kills = 0
        for weapon_stat in weapon_stats:
            if user_id == weapon_stat['user_id'] and weapon_stat['weapon_id'] in weapon_ids:
                kills += weapon_stat['kills']
        return kills
