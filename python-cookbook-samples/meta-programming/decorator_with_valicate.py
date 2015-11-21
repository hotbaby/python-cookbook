#! /usr/bin/env python 
#coding=utf-8

from inspect import signature #TODO Only python 3.x support signature.
from functools import wraps
from twisted.persisted.aot import Instance
import logging

def typeassert(*tr_args, **tr_kwargs):
    
    def decorator(func):
        #If in optimized mode, disable type checking
        if not __debug__:
            return func
        
        #Map function argument names to supplied types
        sig = signature(func)
        bound_types = sig.bind_partial(*tr_args, **tr_kwargs).arguments
        print(bound_types)
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            print(bound_values)
            #Enforce type assertions across supplied arguments
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not Instance(value, bound_types[name]):
                        raise TypeError('Argument {} must be {}'.format(name,bound_types[name]))
            return func(*args, **kwargs)
        return wrapper
    return decorator

@typeassert(int, z=int)
def spam(x, y, z=42):
    print(x, y, z)
    
if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    spam()
