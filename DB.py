import sqlite3
import string
from random import choice
class DB:
    def __init__(self,dbname:str):
        try:
            self.db = sqlite3.connect(dbname)
            self.cursor = self.db.cursor()
        
        except sqlite3.Error:
            print(sqlite3.Error)
    def create_table(self,table:str):
        self.cursor.execute(f'create table if not exists {table}')
        self.db.commit()
    def add_codes(self,site:str,n:int):
        characters = list(string.ascii_uppercase + string.ascii_lowercase + string.digits)
        for i in range(0,n):
            code = ''
            for j in range(0,8):
                code += choice(characters)
            self.cursor.execute('insert into codes(site,code) values(?,?)' , (site,code))
            self.db.commit()
