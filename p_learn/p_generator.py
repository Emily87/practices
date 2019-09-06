L = [x * x for x in range(10)]
#print(L)
g = (x * x for x in range(10))
#print(g)
#创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator
#print(next(g))
#generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误
for n in g:
    print(n)
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)




def triangles():
    p = [1]
    while True:
        yield p#generator函数与普通函数的差别：在执行过程中，遇到yield就中断，下次又继续执行
        p = [1] + [p[i] + p[i+1] for i in range(len(p)-1)] + [1]
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break



if __name__=='__main__':
    o = odd()
    print(next(o))
    print(next(o))




