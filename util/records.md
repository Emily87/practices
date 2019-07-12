records库的使用非常简单且人性化，定义数据库连接串和sql语句，然后将返回值作为rows打印出来，或者输出为文件，没有复杂的orm逻辑，实现逻辑很清晰

import records
db = records.Database('"postgresql://scott:tiger@localhost/test"')
rows = db.query('select * from users')    # or db.query_file('sqls/users.sql')

>>> rows[0]
<Record {"username": "model-t",  "user_email": "model-t@gmail.com"}>

for r in rows:
    print(r.name, r.user_email)
变量:
1.  前带_的变量:  标明是一个私有变量, 只用于标明, 外部类还是可以访问到这个变量
2.  前带两个_ ,后带两个_ 的变量:  标明是内置变量,
3.  大写加下划线的变量:  标明是 不会发生改变的全局变量
函数:
1. 前带_的变量: 标明是一个私有函数, 只用于标明,
2.  前带两个_ ,后带两个_ 的函数:  python中魔法函数
@property装饰器：
把类中的方法作为属性调用
__getattr__
python 对象通过内置成员__dict__来存储成员信息
我们还可以通过重载__getattr__和__setattr__来拦截对成员的访问
ps：'__getattr__'只有在访问不存在的成员时才会被调用
获取属性，仍然调用__getitem__

tablib：用于导出sql查询的结果，导出xls、csv、yaml等格式
import tablib
headers = ('number', 'user', 'sex')
data = [
    ('1', 'lily', '男'),
    ('2', 'lucy', '女'),
]
result = tablib.Dataset(*data, headers=headers)
result.append(['3', 'tom','男'])
result.append_col([30, 20,13], header='Age')
open('test1.xls', 'wb').write(result.xls)  #导出excel表

sqlalchemy：基于sqlalchemy进行封装
create_engine：建立数据库连接引擎




参考：https://www.jianshu.com/p/b730aaf1b826
