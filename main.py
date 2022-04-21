# https://csgo.fastcup.net/match8098261
import json

from helper.calculation_helper import CalculationHelper
from helper.parse_helper import ParseHelper
from helper.request_helper import RequestMock, RequestHelper
from utils.excel import export_to_excel
from utils.exceptions import MatchNotFound
from utils.utils import get_match_id


def main():
    url = 'https://csgo.fastcup.net/match8098261'
    match_id = get_match_id(url)
    if match_id is None:
        raise MatchNotFound
    request_helper = RequestHelper()
    match = request_helper.get_match(match_id)
    match_member_stats = request_helper.get_match_member_stats(match_id)
    match_weapon_stats = request_helper.get_match_weapon_stats(match_id)

    with open('extra_info.json', 'r') as extra_info_fp:
        extra_info = json.load(extra_info_fp)

    match_ = ParseHelper.parse_match(match)
    mms = ParseHelper.parse_match_member_stats(match_member_stats)

    scores = CalculationHelper.calculate_score(mms, match_weapon_stats, extra_info)

    export_to_excel(match_, scores)


if __name__ == '__main__':
    main()
