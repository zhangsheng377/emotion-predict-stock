from pymongo import MongoClient, errors # 树莓派只能通过pip安装3.2版本
from snownlp import SnowNLP
import re

# 等到paddlehub支持树莓派时，就可以用百度paddle的预训练模型，甚至之后可以做个网站或小程序，不断的迁移学习更新paddlehub的与训练模型

exit()

with MongoClient() as client:
    databese = client["xueqiu"]
    sheet = databese["comments"]
    for data in sheet.find():
        sub_text = re.sub(u"<.*?>|\\$.*?\\$|\\&nbsp\\;","", data['text'])
        #if sub_text != data['text']:
        #    print(data['_id'], data['text'], sub_text)
        snownlp_senta=0.5
        try:
            snownlp_senta=SnowNLP(sub_text).sentiments
        except:
            pass
        #print(data['_id'], data['text'],snownlp_senta)
        sheet.update_one(filter={"_id":data['_id']}, update={ "$set": { "text": sub_text, "snownlp_senta": snownlp_senta } })
        print(data['_id'], sub_text, snownlp_senta)

