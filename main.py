# https://csgo.fastcup.net/match8098261
from request_helper import RequestMock


if __name__ == '__main__':
    match = RequestMock.get_match(8098261)
    print(match['id'])
    print([{'id': member['private']['user']['id'], 'nickname': member['private']['user']['nickName']} for member in match['members']])
