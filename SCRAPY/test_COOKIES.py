import requests
from UA import Agents


# print(Agents().get_random_agent())
# print(Agents().agents)

from COOKIES import Cookies

headers = {
    'User-Agent': Agents().get_random_agent()
}
# print(Cookies(headers=headers).cookie)

api_url = 'https://xueqiu.com/statuses/search.json?sort=time&source=all&q=01810&count=10&page=1'
session = requests.session()
session.cookies = Cookies(headers=headers).cookie
api_request = session.get(url=api_url, headers=headers, timeout=10)
print(api_request.status_code)
