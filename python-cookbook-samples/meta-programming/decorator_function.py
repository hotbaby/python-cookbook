#!/usr/bin/env python
# coding=utf-8

'''
    function decorator:
        It is function. It accept func as it's parameter and return a function.
        Do save the function meta data through '@wraps'
'''

import time
from functools import wraps

def time_cost(func):
    '''
    Decorator that reports the excution time.
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, (end-start))
        return result

    return wrapper

@time_cost
def countdown(n):
    '''
    Counts down
    '''
    print('call %s' % countdown.__name__)
    while n:
        n -= 1

if __name__ == '__main__':
    countdown(1000)
    countdown.__name__
    countdown.__doc__

    '''
    Cancel the decorator
    '''
    #orig_countdown = countdown.__wrapped__
    #orig_countdown(1)

