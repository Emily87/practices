from collections import Iterable,Iterator
print(isinstance([],Iterable))
# print(isinstance({},Iterable))
# print(isinstance({},Iterable))
# print(isinstance('abc', Iterable))
# print(isinstance((x for x in range(10)), Iterable))
# print( isinstance(100, Iterable))
print(isinstance([],Iterator))
# print( isinstance({}, Iterator))
print(isinstance(iter([]), Iterator))
for x in [1, 2, 3, 4, 5]:
    pass
it = iter([1, 2, 3, 4, 5])
while True:
    try:
        # 获得下一个值:
        x = next(it)
        print(x)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break

# 小结
# 凡是可作用于for循环的对象都是Iterable类型；
#
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
#
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。