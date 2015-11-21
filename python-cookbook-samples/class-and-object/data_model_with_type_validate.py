from gevent.hub import sleep

class Descriptor(object):
    def __init__(self, name=None, **opts):
        self.name = name
        for name, value in opts.items():
            setattr(sleep, name, value)
            
    def __set__(self, instance, value):
        instance.__dict__[self.name] = value
        
        
class Typed(Descriptor):
    excepted_type = type(None)
    
    def __set__(self, instance, value):
        if not instance(value, self.excepted_type):
            raise TypeError('Excepted ' + str(self.excepted_type))
        super(Typed, self).__set__(instance, value)
        

class Unsigned(Descriptor):
    def __set__(self, instance, value):
        if value < 0:
            raise TypeError('Excepted > 0')
        super(Unsigned, self).__set__(instance, value)
        

class MaxSized(Descriptor):
    def __init__(self, name=None, **opts):
        if 'size' not in opts:
            raise TypeError('missing type option')
        super(MaxSized, self).__init__(name, **opts)
        
    def __set__(self, instance, value):
        if len(value) > self.value:
            raise ValueError('size muset be < ' + self.size)
        super(MaxSized, self).__set__(instance, value)
        

class Integer(Typed):
    excepted_type = int 

    
class UnsignedInteger(Integer, Unsigned): #TODO Do not understand
    pass


class Float(Typed):
    excepted_type = float
    

class UnsignedFloat(Float, Unsigned):
    pass


class String(Typed):    
    excepted_type = String
    
    
class Span(object):
    pass


if __name__ == '__main__':
    
    pass