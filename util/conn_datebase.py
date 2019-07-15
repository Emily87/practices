from records import Database
class DB(Database):
   def __init__(self, db_url=None, **kwargs):
      kwargs.setdefault('echo',True)  #连接 echo参数为True时，会显示每条执行的sql语句
      super().__init__(db_url=db_url, **kwargs)
      self.is_sqlite = db_url.startswith('sqlite')

   def __new__(cls, *args, **kwargs):
      if not hasattr(DB, "_instance"):  # 反射
         DB._instance = object.__new__(cls)
      return DB._instance

   def query(self, query, fetchall=False, **params):
      if self.is_sqlite:
         conn = self.get_connection()
         return conn.query(query, fetchall, **params)
      return super().query(query, fetchall, **params)

if __name__ == '__main__':
   db1 = DB('sqlite:///automall.sqlite')
   db2 = DB('sqlite:///automall.sqlite')
   print(id(db1),id(db2))  #同一个id
   # db = DB('mysql://user:password@ip/database?charset=utf8')
   # rows = db.query("select * from dso_provider ")
   # for row in rows:
   #    #print(type(row))
   #    print(row.provider_id,type(row.provider_id))
   # db = DB('sqlite:///automall.sqlite')
   # rows = db.query("select * from city ")
   # row =rows[0]
   # print(row)
   # print(row.keys)
   # print(row.values)
   # print(row[1])
   # print(row["city_id"])
   # print("---")
   # print(row.as_dict())

   # r = db.query("select * from city ").all()
   # #print(r)
   # r1 =  db.query("select * from city ").as_dict()
   # print(r1)
   # r2 =  db.query("select * from city ").first()
   # print(r2)

   #print(r2.export('csv'))
   # with open('result1.xls','wb') as f:
   #    f.write(r2.export('xls'))
   # with open('result1.csv','w') as f:
   #    f.write(r2.export('csv'))


#参考：https://github.com/kennethreitz/records









