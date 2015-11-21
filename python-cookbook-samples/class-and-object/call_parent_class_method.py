
class SuperClass(object):
    def __init__(self, *args, **kwargs):
        self.x  = 0
    
        
class SubClass(SuperClass):
    def __init__(self, *args, **kwargs):
        self.y = 0
        super(SubClass, self).__init__(*args, **kwargs)


class Proxy(object):
    def __init__(self, obj):
        self._obj = obj
        
    def __getattr__(self, name):
        return getattr(self._obj, name)
    
    def __setattr__(self, name, value):
        if name.start_with('_'):
            return super(Proxy, self).__setattr__(name, value)
        else:
            return setattr(self._obj, name, value)


if __name__ == '__main__':
    
    pass
    
