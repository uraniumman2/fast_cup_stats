from helper.static import Weapon, Role


class CalculationHelper:

    @staticmethod
    def calculate_score(match_member_stats, weapon_stats, extra_info):
        match_member_stats_ = {}
        for mms in match_member_stats:
            basic = CalculationHelper.calculate_basic_score(mms,
                                                            extra_info)
            extra = CalculationHelper.calculate_extra_score(mms,
                                                            weapon_stats,
                                                            extra_info)
            score = {
                'basic': basic,
                'extra': extra,
                'total': basic + extra
            }
            match_member_stats_[mms['user_id']] = score

        return match_member_stats_

    @staticmethod
    def calculate_basic_score(mms, extra_info):
        user_id = mms['user_id']
        role = extra_info.get(str(user_id))
        if role is None:
            return 0
        kd = mms['k'] / mms['d'] if mms['d'] != 0 else 0
        adr = mms['adr'] / 100

        fk = mms['fk'] / mms['k'] if mms['k'] != 0 else 0
        fd = mms['fd'] / mms['d'] if mms['d'] != 0 else 0

        v5, v4, v3, v2, v1 = mms['1v5'], mms['1v4'], mms['1v3'], mms['1v2'], mms['1v1']
        m5, m4, m3, m2, m1 = mms['m5'], mms['m4'], mms['m3'], mms['m2'], mms['m1']

        clutch_rate = v5 * 0.1 + v4 * 0.08 + v3 * 0.06 + v2 * 0.04 + v1 * 0.02

        if role == Role.SUPPORT:
            clutch_rate *= 1.21
            fd = 0

        multi_kill = m5 * 0.05 + m4 * 0.04 + m3 * 0.03 + m2 * 0.02 + m1 * 0.01

        basic = kd * 0.2 + adr * 0.2 + fk - fd + clutch_rate + multi_kill
        return basic

    @staticmethod
    def calculate_extra_score(mms, weapon_stats, extra_info):
        user_id = mms['user_id']
        extra_info = extra_info.get(str(user_id))
        if extra_info is None:
            return 0
        role = extra_info['role']
        kills = mms['k']
        if role == Role.AWP:
            awp = CalculationHelper.get_weapon_kills_(user_id=user_id,
                                                      weapon_stats=weapon_stats,
                                                      weapon_ids=[Weapon.AWP])
            extra = awp / (kills * 2) if kills != 0 else 0
        elif role == Role.RIFFLE:
            riffle = CalculationHelper.get_weapon_kills_(user_id=user_id,
                                                         weapon_stats=weapon_stats,
                                                         weapon_ids=[Weapon.AK47, Weapon.M4A4, Weapon.M4A1_S])
            extra = riffle / (kills * 3) if kills != 0 else 0
        else:
            extra = 0.2

        grenade = extra_info['grenade']
        if role == Role.SUPPORT:
            if grenade:
                extra += 0.2
            else:
                extra -= 0.2
        else:
            if grenade:
                extra += 0.1

        if extra_info['capitan']:
            extra += 0.1

        return extra

    @staticmethod
    def get_weapon_kills_(user_id, weapon_stats, weapon_ids):
        kills = 0
        for weapon_stat in weapon_stats:
            if user_id == weapon_stat['user_id'] and weapon_stat['weapon_id'] in weapon_ids:
                kills += weapon_stat['kills']
        return kills
