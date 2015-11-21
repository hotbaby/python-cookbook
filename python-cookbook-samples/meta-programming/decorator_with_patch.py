
def log_getattribute(cls):
    
    orig_getattribute = cls.__getattribute__
    def new_getattribute(self, name):
        print('Gettging:', cls.__name__+':'+name)
        return orig_getattribute(self, name)
    cls.__getattribute__ = new_getattribute
    return cls

@log_getattribute
class Span(object):
    def __init__(self, x):
        self.x = x
    
    def span(self):
        pass

if __name__ == '__main__':
    ins = Span(100)
    ins.x
    ins.span()
    