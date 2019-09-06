class Student(object):

    def __init__(self):
        self.name = 'Michael'

    # def __getattr__(self, attr):
    #     if attr=='score':
    #         return 99

    def __getattr__(self, attr):
        if attr == 'age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path
    __repr__ = __str__

if __name__ =='__main__':
    s = Student()
    #只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找
    print(s.name)
    #print(s.score) #当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性
    print(s.age())#返回函数
    #注意到任意调用如s.abc都会返回None，这是因为我们定义的__getattr__默认返回就是None。要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError的错误：
    #print(s.abc)
    c = Chain()
    print(c.status.user.timeline.list)