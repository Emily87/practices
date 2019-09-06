# s = 'a, B'
# print(s.capitalize())
from functools import reduce
L1 = ['adam', 'LISA', 'barT']
def normalize(name):
    return name.capitalize()
# def f(x,y):
#     return x*y
# def  prod(L):
#     return reduce(f,L)
def prod(L):
    return reduce(lambda x,y:x*y,L)

from functools import reduce
def str2float(s):
    def fn(x,y):
            return x*10+y
    n=s.index('.')
    print(n)
    s1=list(map(int,[x for x in s[:n]]))
    print(s1)
    s2=list(map(int,[x for x in s[n+1:]]))
    print(s2)
    print(type(reduce(fn,s1)),type(reduce(fn,s2)/10**len(s2)))
    return reduce(fn,s1)+reduce(fn,s2)/10**len(s2)








if __name__=='__main__':
    #print(normalize('abc'))
    #print(list(map(normalize,L1)))
    L = [1,2,3,4]
    print(prod(L))
    print('str2float(\'123.456\')=', str2float('123.456'))

