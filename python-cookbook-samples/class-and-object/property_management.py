
class Person(object):
    
    def __init__(self, first_name):
        self._first_name = first_name
    
    @property    
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, first_name):
        if not isinstance(first_name, str):
            raise TypeError('Expect string.')
        self._first_name = first_name
        
    @first_name.deleter 
    def first_name(self):
        raise AttributeError('Can not delete first_name attribue.')
    
if __name__ == '__main__':
    ins = Person('Ming')
    print(ins.first_name)
    ins.first_name = 'Wang'
    print(ins.first_name)
    del ins.first_name
