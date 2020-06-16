import sqlite3
import pandas

from ._DataBase import DataBase


class DataBaseSqlite3(DataBase):
    def __init__(self, database_name, sheet_name):
        self.__databese = sqlite3.connect(database_name)
        self.__sheet_name = sheet_name
        df_data_read = pandas.read_sql(sql="SELECT * FROM "+self.__sheet_name+" LIMIT 1", con=self.__databese)
        self.__columns = df_data_read.columns
        self.__id = self.__columns[0]

    def insert(self, document):
        try:
            names = ""
            masks = ""
            for name in document.keys():
                names += name+", "
                masks += "?,"
            names = names[:-2]
            masks = masks[:-1]

            values=[]
            for value in document.values():
                values.append(value)
            values = tuple(values)

            cursor = self._databese.cursor()
            cursor.execute("INSERT INTO "+self.__sheet_name+"("+names+") VALUES("+masks+")", values)
            self.__databese.commit()
            return True
        except Exception as e:
            pass
        return False

    def find(self, filter=None, sort=None):
        sql = "SELECT * FROM " + self.__sheet_name
        if sort != None and sort[0][0] in self.__columns:
            sql += " ORDER BY " + sort[0][0]
            if sort[0][1] == -1:
                sql += " DESC"
            else:
                sql += " ASC"
        
        return pandas.read_sql(sql=sql, con=self.__databese)

    def find_one(self, filter=None, sort=None):
        sql = "SELECT * FROM " + self.__sheet_name
        if sort != None and sort[0][0] in self.__columns:
            sql += " ORDER BY " + sort[0][0]
            if sort[0][1] == -1:
                sql += " DESC"
            else:
                sql += " ASC"
        
        sql += " LIMIT 1"
        
        return pandas.read_sql(sql=sql, con=self.__databese).iloc[0]

    def update_one(self, filter, update):
        print("WARNING: DataBaseSqlite3 update_one does not complete.\n")
        pass

    def delete(self, filter):
        print("WARNING: DataBaseSqlite3 delete does not complete.\n")
        pass
