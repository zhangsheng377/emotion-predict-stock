from SCRAPY.UA import Agents
from SCRAPY.COOKIES import Cookies
from SCRAPY.SENTA import SentaFactory
from SCRAPY.BLACKLIST import blackList
from SCRAPY.BLACKLIST import blackBlackList
from DATABASE import DataBaseFactory

import time
import requests
import random
import json
import re
import pandas as pd


api_url = 'https://xueqiu.com/statuses/search.json?sort=time&source=all&q=01810&count=10&page=1'


def scrapy_xueqiu(needSaveToCsv=False):
    headers = {
        'User-Agent': Agents().get_random_agent()
    }

    session = requests.session()

    try:
        session.cookies = Cookies(headers=headers).cookie
        api_request = session.get(url=api_url, headers=headers, timeout=10)
    except:
        print("session error!")
        return

    if api_request.status_code != 200:
        print("api_request.status_code:", api_request.status_code)
        return
    try:
        json_api_request = json.loads(api_request.text)
        list_data = json_api_request['list']
    except:
        print("json load error!")
        return

    senta = SentaFactory(model="snownlp")

    dataSheet = DataBaseFactory(
        database_name="xueqiu", sheet_name="comments", model="pymongo")

    for comment in list_data:
        sub_text = re.sub(u"<.*?>|\\$.*?\\$|\\&nbsp\\;", "", comment['text'])
        sub_text = sub_text.strip()

        if sub_text == "":
            continue

        if comment['user_id'] in blackBlackList:
            continue

        if comment['user_id'] in blackList and '小米' not in sub_text:
            continue

        last_record_text = dataSheet.find_one(sort=[('_id', -1)])['text']
        if sub_text == last_record_text:
            print('丢弃重复最新内容\n')
            continue

        senta_score = senta.sentiments(doc=sub_text)

        insertResult = dataSheet.insert({'_id': comment['id'], 'user_id': comment['user_id'],
                                         'time': comment['created_at'], 'text': sub_text, 'snownlp_senta': senta_score, 'raw': str(comment)})
        if insertResult:
            print(sub_text, senta_score)
            print(comment['id'], comment['user_id'], '评论插入成功\n')
        else:
            print(comment['id'], '已经存在于数据库\n')

    if needSaveToCsv:
        df = pd.DataFrame(list(dataSheet.find(sort=[('_id', -1)])))
        df.set_index(keys='_id', inplace=True)
        df.to_csv("data_pd.csv")


def timedTask(gapSecond=1200):
    while True:
        scrapy_xueqiu(needSaveToCsv=True)
        sleepSecond = gapSecond + random.randint(0, 300)
        print(time.asctime(time.localtime(time.time())),
              "    sleep {} s".format(sleepSecond))
        time.sleep(sleepSecond)


if __name__ == '__main__':
    timedTask()
