from lxml.html.builder import INS

class NoInstance(type):
    
    def __call__(self, *args, **kwargs):
        raise TypeError('Cannot instantiate directly')
    

class Singleton(type):
    def __init__(self, *args, **kwargs):
        super(Singleton, self).__init__(*args, **kwargs)
        self ._instance = None
        
    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = super(Singleton, self).__call__(*args, **kwargs)
            return self._instance
        else:
            return self._instance


class Span(object):
    __metaclass__ = Singleton
    
    def __init__(self, *args, **kwargs):
        pass

class Test(object):
    pass


if __name__ == '__main__':
    ins1 = Span()
    ins2 = Span()
    print(ins1 == ins2)
    
    ins1 = Test()
    ins2 = Test()
    print(ins1 == ins2)