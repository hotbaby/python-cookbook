#! /usr/bin/env python
#coding=utf-8

from functools import wraps, partial
import logging

def attatch_wrapper(obj, func=None):
    if func is None:
        return partial(attatch_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func

def logged(level, name=None, msg=None):
    '''
    
    '''
    def decorator(func):
        global loglevel, logmsg
        loglevel = level
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = msg if msg else func.__name__
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(loglevel, logmsg)
            return func(*args, **kwargs)
        
        @attatch_wrapper(wrapper)
        def set_level(newlevel):
           #nonlocal level  #python 2.x does not support nonlocal syntax
            global loglevel
            loglevel = newlevel
        
        @attatch_wrapper(wrapper)
        def set_message(newmsg):
            #nonlocal logmsg #python 2.x  does not support nonlocal syntax
            global logmsg
            logmsg = newmsg
            
        return wrapper
    return decorator

@logged(logging.DEBUG)
def add(x,y):
    return x+y

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    
    add(1, 1)
    add.set_level(logging.WARN)
    add(1, 1)