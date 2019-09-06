s = 0
def createCounter():
    def counter():
        global  s#引用全局变量
        s = s+1
        return s
    return counter
def createCounter():
    s = [0]
    def counter():
        s[0] = s[0]+1
        return s[0]
    return counter

if __name__ == '__main__':
    counterA = createCounter()
    print(counterA())
    print(counterA())
    print(counterA())

    counterA = createCounter()
    print(counterA())
    print(counterA())
    print(counterA())