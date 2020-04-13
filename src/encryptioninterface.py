from abc import ABC, abstractmethod

class EncryptionInterface(ABC):
    
    @abstractmethod
    def encrypt(self, message, key=0):
        
        pass
    
    @abstractmethod
    def decrypt(self, message, key=0):
        
        pass
    
    