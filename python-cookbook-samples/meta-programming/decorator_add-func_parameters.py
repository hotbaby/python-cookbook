from functools import wraps
import inspect

def optional_debug(func):
    if 'debug' in inspect.getargspec(func).args:
        raise TypeError('debug argument already exist.')

    @wraps(func)
    #def wrapper(*args, debug=True, **kwargs): # TODO python 2.x does not support this syntax
    def  wrapper(*args, **kwargs):
        
        #if debug == True: #TODO Only use  in python 2.x version
         #   print(func.__name__)
        
        return func(*args, **kwargs)
    return wrapper

@optional_debug
def span():
    pass

if __name__ == '__main__':
    span()
    