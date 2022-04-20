class CalculationHelper:

    @staticmethod
    def calculate_basic_score(match_member_stats):
        match_member_stats_ = []
        for mms in match_member_stats:
            kd = mms['k'] / mms['d']
            adr = mms['adr']
            fk = mms['fk'] * (1 - 1 / mms['k'])
            fd = mms['fd'] * (1 - 1 / mms['d'])
            v5, v4, v3, v2, v1 = mms['1v5'], mms['1v4'], mms['1v3'], mms['1v2'], mms['1v1']
            m5, m4, m3, m2, m1 = mms['m5'], mms['m4'], mms['m3'], mms['m2'], mms['m1']
            basic = kd * 0.2 + adr * 0.2 + fk + fd + \
                    v5 * 0.1 + v4 * 0.08 + v3 * 0.06 + v2 * 0.04 + v1 * 0.02 + \
                    m5 * 0.05 + m4 * 0.04 + m3 * 0.03 + m2 * 0.02 + m1 * 0.01
            info = {
                'user_id': mms['user_id'],
                'basic': basic,
            }
            match_member_stats_.append(info)
        return match_member_stats_
