from abc import abstractmethod, ABCMeta


#Can not be instanced
class IStream(object):
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def read(self, maxbytes):
        pass
    
    @abstractmethod
    def write(self, data):
        pass
    

class SocketStream(IStream):
    def read(self, maxbytes=-1):
        pass
    
    def write(self, data):
        pass
    