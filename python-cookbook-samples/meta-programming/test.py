#! /usr/bin/env python 
#coding=utf-8

import logging

def make_counter():
    global number
    number = 0
    
    def counter():
        global number
        number += 1
        print(number)
        return number
    return counter

def func(*args, **kwargs):
    print(args)
    print(kwargs)
    print(kwargs['debug'])
    
    
class Test(object):
    def __prepare__(cls):
        print('Call __prepare__  function.')
        
    def __new__(cls):
        print('Call __new__ function.')
        
    def __init__(self):
        print('Call __init__ function.')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    
    Test()
    