from caesarcipher_algo import CaesarCipher
from vigenerecipher_algo import VigenereCipher
from enigmam3_algo import EnigmaM3
from des_algo import DES
from aes_algo import AdvancedEncryptionStandard

test = AdvancedEncryptionStandard()

message = input("Enter text to be encrypted\n")

key = input("Enter the key\n")


encryptedMessage = test.encrypt(message, key)
decryptedMessage = test.decrypt(encryptedMessage, key)
print("The encrypted message is: " + str(encryptedMessage))

print("Decrypted message: " + decryptedMessage)

