"""Implementation of the RSA encryption method"""

import logging
import logging.handlers
from Crypto.PublicKey import RSA
from encryptioninterface import EncryptionInterface


class RSAAlgo(EncryptionInterface):

    def __init__(self):

        self.logger = logging.getLogger(__name__)
        fh = logging.handlers.RotatingFileHandler('logs/' + __name__ + '.log', maxBytes=10000000, backupCount=100)
        fh.setFormatter(logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(name)s - %(message)s'))
        self.logger.addHandler(fh)


    def encrypt(self, message, key=0):


        if not isinstance(message, str):

            self.logger.error("Error during the encryption of a message with RSA. The message must be a string")
            return False

        if not isinstance(key, bytes):

            self.logger.error("Error during the encryption of a message with RSA. The key must be a bytes object")
            return False

        publicKey = RSA.importKey(key)
        encryptedMessage = publicKey.encrypt(bytes(message, encoding="utf-8"), b"random")


        return encryptedMessage[0].hex()

    def decrypt(self, message, key=0):


        if not isinstance(message, str):

            self.logger.error("Error during the decryption of a message with RSA. The message must be a string")
            return False

        if not isinstance(key, bytes):

            self.logger.error("Error during the decryption of a message with RSA. The key must be a bytes object")
            return False
        
        message = bytes.fromhex(message)

        privateKey = RSA.importKey(key)
        decryptedMessage = privateKey.decrypt(message)

        return decryptedMessage.decode("utf-8")

    def generateKeysPair(self):

        newKey = RSA.generate(4096, e=65537)
        privateKey = newKey.exportKey("PEM")
        publicKey = newKey.publickey().exportKey("PEM")

        return (privateKey, publicKey)
