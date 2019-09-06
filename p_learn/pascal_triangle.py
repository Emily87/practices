
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
#杨辉三角
def triangles():
    p = [1]
    while True:
        yield p
        p = [1] + [p[i] + p[i + 1] for i in range(len(p) - 1)] + [1]
n = 0
tri = triangles()
for i in tri:
    print(i)
    n = n + 1
    if n == 10:
        break

# p =[1]
# p2 = [1,1]
# p3 = [1]+[p2[0]+p2[1]]+[1]
# print(p3,type(p3))
# p4 = [1]+[p3[0]+p3[1]]+[p3[1]+p3[2]]+[1]
# print(p4)
# p5 = [1]+[p4[0]+p4[1]]+[p4[1]+p4[2]]+[p4[2]+p4[3]]+[1]
# print(p5)
# p = [1]+[p[i]+p[i+1] for i in range(len(p)-1)]+[1]
# b=[1,2,3,4,5]
# b = [b[i] + b[i + 1] for i in range(3)]
# print(b)
# [3,5,7]