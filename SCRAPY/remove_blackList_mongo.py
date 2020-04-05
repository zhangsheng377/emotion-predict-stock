import re

from BLACKLIST import blackList
from BLACKLIST import blackBlackList
from DATABASE import DataBaseFactory

# 模糊匹配查询
# 在mongo中这样实现
# {'filed':/value/}

p = re.compile(r'^((?!小米).)*$')
# p = re.compile(r'^(?!.*小米)')
print(p.search("error123abc"))
print(p.search("小米error123abc"))
print(p.search("error1小米23abc"))
print(p.search("小米error123abc小米"))


dataSheet = DataBaseFactory(database_name="xueqiu",
                            sheet_name="comments", model="pymongo")

for blackUserId in blackList:
    # print(sheet.find_one({'user_id': blackUserId,
    #                   'text': {'$regex': '小米'}}, {'text': 1}))
    # try:
    #print(sheet.find_one({'user_id': blackUserId,'text': {'$regex': '(!小米)'}}, {'text': 1}))
    #print(sheet.find_one({'user_id': blackUserId,'text': {'$regex': p}}, {'text': 1}))
    #   pass
    # except:
    #   print('不包含小米的 user_id:{} 清理完成.'.format(blackUserId))

    data_list = list(dataSheet.find(filter={'user_id': blackUserId}))
    print(len(data_list))

    for data in data_list:
        if '小米' not in data['text']:
            dataSheet.delete(filter={'_id': data['_id']})

    data_list = list(dataSheet.find(filter={'user_id': blackUserId}))
    print(len(data_list))

for blackBlackUserId in blackBlackList:
    data_list = list(dataSheet.find(filter={'user_id': blackBlackUserId}))
    print(len(data_list))

    for data in data_list:
        dataSheet.delete(filter={'_id': data['_id']})

    data_list = list(dataSheet.find(filter={'user_id': blackBlackUserId}))
    print(len(data_list))
