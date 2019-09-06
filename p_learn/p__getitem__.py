class Fi(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a

class Fib(object):
    def __getitem__(self, n):
        if isinstance(n,int):
            a,b = 1,1
            for i in range(n):
                a,b = b,a+b
            return a
        if isinstance(n,slice):
            start = n.start
            stop = n.stop
            #print(start,stop)
            if start is None:
                start = 0
            a,b = 1,1
            L =[]
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a,b = b,a+b
                #print(a)
            return L

if __name__ == '__main__':
    f1 = Fi()
    #print(f1[0])
    #print(list(range(100))[5:10])
    f = Fib()
    #f[1:4]
    print(f[3:6])

