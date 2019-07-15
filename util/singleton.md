__new__是在实例创建之前被调用的，因为它的任务就是创建实例然后返回该实例，是个静态方法
__init__是当实例对象创建完成后被调用的，然后设置对象属性的一些初始值
__new__所接收的第一个参数是cls，而__init__所接收的第一个参数是self。这是因为当我们调用__new__的时候，该类的实例还并不存在（也就是self所引用的对象还不存在），所以需要接收一个类作为参数，从而产生一个实例。而当我们调用__init__的时候，实例已经存在，因此__init__接受self作为第一个参数并对该实例进行必要的初始化操作。这也意味着__init__是在__new__之后被调用的
class Book(object):
    def __new__(cls, title):
        print('__new__')
        cls.m = 2
        print(super().__new__(cls))
        #return super().__new__(cls)

    def __init__(self, title):
        print(self)
        print('__init__')
        self.title = title


b = Book('The  Book')
print(b.title,b.m)
