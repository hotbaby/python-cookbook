
class Pair(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return '({0.x!s}, {0.x!s})'. format(self) 
    
    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)
    


class Date(object):
    
    _formats = {
        'ymd' : '{d.year}-{d.month}-{d.day}',
        'mdy' : '{d.month}-{d.day}-{d.year}',
        'dmy' : '{d.day}-{d.month}-{d.year}',        
    }
    
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        
    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = self._formats[code]
        return fmt.format(d=self)

if __name__ == '__main__':
    ins = Pair(100, 100)
    print(ins)
    print(repr(ins))

    d = Date('2004', '12', '12')
    print(format(d))
    print(format(d, 'mdy'))
    print(format(d, 'dmy'))
    