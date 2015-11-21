import time
from functools import wraps
from gevent.hub import sleep

def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(end-start)
        return result
    return wrapper

class Span(object):
    
    def instance_method(self, n):
        print(self, n)
        while n > 0:
            n -= 1
    
    ''''
    The order of classmethod and timethis must not change.
    Other than, it will throw exceptin.
    '''
    @classmethod
    @timethis
    def class_method(cls, n):
        print(cls, n)
        while n > 0:
            n -= 1
            

if __name__ == '__main__':
    s = Span()
    s.instance_method(1000)
    s.class_method(1000)
