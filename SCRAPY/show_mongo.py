from DATABASE import DataBaseFactory

dataSheet = DataBaseFactory(database_name="xueqiu",
                            sheet_name="comments", model="pymongo")
for data in dataSheet.find():
    print(data)
