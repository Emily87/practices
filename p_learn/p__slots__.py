#限制实例的属性
#只允许对Student实例添加name和age属性
#定义一个特殊的__slots__变量，来限制该class实例能添加的属性
# 由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。
# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
class Student(object):
    __slots__ = ('name', 'age')
class GraduateStudent(Student):
    __slots__ = ('glass')

if __name__=='__main__':
    s = Student()
    s.name = 'm'
    s.age = 15
    print(s.name,s.age)
    #.score = 90
    g = GraduateStudent()
    # g.score = 90
    # print(g.score)
    g1 = GraduateStudent()
    g1.glass = '1'
    g.score = 90