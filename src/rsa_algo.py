import logging
import logging.handlers
from encryptioninterface import EncryptionInterface

# =============================================================================
# Implementation of the RSA encryption method
# =============================================================================

class RSA(EncryptionInterface):
    
    def __init__(self):
        
        self.logger = logging.getLogger(__name__)
        fh = logging.handlers.RotatingFileHandler('logs/' + __name__ + '.log', maxBytes=10000000, backupCount=100)
        fh.setFormatter(logging.Formatter(fmt = '%(asctime)s - %(levelname)s - %(name)s - %(message)s'))
        self.logger.addHandler(fh)
        
    
    def encrypt(self, message, key=0):
        
        
        if not isinstance(message, str):
            
            self.logger.error("Error during the encryption of a message with DES. The message must be a string")
            return False
        
        if not isinstance(key, str) or len(bytes(key, encoding='utf-8')) not in (16, 24, 32):
            
            self.logger.error("Error during the encryption of a message with DES. The key must be a string in ASCII format of length 16, 24 or 32")
            return False
        
        
        
    
        return encryptedMessage
    
    def decrypt(self, message, key=0):
        
        
        if not isinstance(message, bytes):
            
            self.logger.error("Error during the decryption of a message with DES. The message must be a string")
            return False
        
        if not isinstance(key, str) or len(bytes(key, encoding='utf-8')) not in (16, 24, 32) :
            
            self.logger.error("Error during the decryption of a message with DES. The key must be an string in ASCII format of length 16, 24 or 32")
            return False
        
        
        
        return decryptedMessage.decode("utf-8")