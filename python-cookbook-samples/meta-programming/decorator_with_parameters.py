#!/usr/bin/env python
# coding=utf-8

'''
def func(a,b):
    pass

func = decorate(x,y,z)(func)
'''
from functools import wraps
import logging

def logged(level, name=None, msg=None):
    '''
    Add logging to a function. level is the logging level, 
    name is the logger name, msg is the logger message.If the 
    name and msg is not specified, they default to the function's
    module and name
    '''
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = msg if msg else func.__name__
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)
        return wrapper
    return decorate

@logged(logging.DEBUG)
def add(x, y):
    return x+y

@logged(logging.DEBUG)
def span():
    print('Spam!')

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    add(1,1)
