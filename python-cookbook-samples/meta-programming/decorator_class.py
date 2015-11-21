import types
from functools import wraps


class A(object):
    #Decorator as an instance method
    def decorator1(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    
    #Decorator as a class method
    @classmethod
    def decorator2(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper


class Profiled(object):

    def __init__(self, func):
        #wraps(func)(self) #TODO python 2.x does not support
        self.ncalls = 0
        self.wrapper = func
        
    def __call__(self, *args, **kwargs):
        self.ncalls += 1
        #return self.__wrapped__(*args, **kwargs)
        return self.wrapper(*args, **kwargs)
    
    def __get__(self, instance, cls): #TODO Does not understand
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)


class Span(object):
    @Profiled
    def bar(self, x):
        print(self, x)


@Profiled
def add(x, y):
    return x+y

if __name__ == '__main__':
    print('Add call times %s' % (add.ncalls))

