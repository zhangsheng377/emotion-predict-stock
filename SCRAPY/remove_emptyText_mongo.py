from DATABASE import DataBaseFactory

# 模糊匹配查询
# 在mongo中这样实现
# {'filed':/value/}

dataSheet = DataBaseFactory(database_name="xueqiu",
                            sheet_name="comments", model="pymongo")

data_list = list(dataSheet.find())
print(len(data_list))

dataSheet.delete(filter={'text': ""})

data_list = list(dataSheet.find())
print(len(data_list))
