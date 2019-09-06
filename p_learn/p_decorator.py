import functools
def log(*text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print(func.__name__,'begin',*text)
            func(*args,**kw)
            print(func.__name__,'end',*text)
        return wrapper
    return decorator

#@log('execute')
@log()
def foo():
    print('foo is running...')
if __name__=='__main__':
    f=foo
    f()

