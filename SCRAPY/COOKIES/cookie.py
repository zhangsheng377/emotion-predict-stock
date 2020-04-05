import requests
import pickle

index_url = 'https://xueqiu.com/'


def get_and_save_cookis(headers):
    session = requests.session()
    first_request = session.get(url=index_url, headers=headers, timeout=10)
    with open("_COOKIES", 'wb') as f:
        pickle.dump(first_request.cookies, f)
    return first_request.cookies
