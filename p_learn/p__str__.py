from collections import Iterable,Iterator
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name=%s)' % self.name
    __repr__ = __str__

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 10: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a
if __name__ =='__main__':
    s = Student('mm')
    #print(s)
    f = Fib()
    for i in f:
        print(i)
    # print(next(f))
    # print(next(f))
    #print(f[5])
    # print(isinstance(f, Iterable))
    # print(isinstance(f, Iterator))
    print(f[2])


