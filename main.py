from pprint import pprint
import time
from urllib.parse import urlencode
import requests

AUTHORIZE_URL = 'https://oauth.vk.com/authorize'
CLIENT_ID = 6183616
ACCESS_TOKEN = '' # enter your token here


def auth():
    auth_data = {
        'client_id': CLIENT_ID,
        'display': 'popup',
        'response_type': 'token',
        'scope': 'status,friends',
        'v': '5.68'
    }
    token_url = '?'.join((AUTHORIZE_URL, urlencode(auth_data)))
    return token_url


def get_friends(user_id):
    params = {
        'user_id': user_id,
        'access_token': ACCESS_TOKEN,
        'v': '5.68'
    }
    response = requests.get('https://api.vk.com/method/friends.get', params)
    if user_id == 0:
        friends = dict.fromkeys(response.json()['response']['items'])
    else:
        friends = response.json()['response']['items']
    return friends


def get_mutual_friends():
    friends = get_friends(0)
    for user in friends.keys():
        try:
            friends[user] = get_friends(user)
            time.sleep(0.35)
        except KeyError:
            pass
    # none_friends = [f for f in friends.keys() if friends[f] == None]
    # for f in none_friends:
    #     friends[f] = get_friends(f)
    #     time.sleep(0.35)  # ничего не помогает, исключения всё равно выскакивают, я не знаю что тут сделать можно.
    # for f in friends.keys():
    #     n = 0
    #     while n <= len(friends.keys()):
    #         try:
    #             result = list(set(friends[f]) & set(friends[n]))
    #             n += 1
    #             print(result)
    #         except Exception:
    #             pass
    # pprint(friends)

get_mutual_friends()
