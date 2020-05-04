from caesarcipher_algo import CaesarCipher
from vigenerecipher_algo import VigenereCipher
from enigmam3_algo import EnigmaM3
from des_algo import DES
from aes_algo import AdvancedEncryptionStandard
from blowfish_algo import Blowfish
from rsa_algo import RSAAlgo
from md5_algo import MD5
from sha_algo import SHA

msg1 = "Premier message, uniquement composé de lettres de l'alphabet"
msg2 = "Deuxième message, avec des caractères spéciaux"

t1 = CaesarCipher()
t2 = VigenereCipher()
t3 = EnigmaM3()
t4 = DES()
t5 = AdvancedEncryptionStandard()
t6 = Blowfish()
t7 = RSAAlgo()
t8 = MD5()
t9 = SHA()


print("BLOWFISH")
encryptedMsg1 = t6.encrypt(msg1, "123456789123456789123456")
encryptedMsg2 = t6.encrypt(msg2, "CLE PLUS LONGUE , mais toujours dans la limite")
print("msg1, encrypted: " + str(encryptedMsg1))
print("msg2, encrypted: " + str(encryptedMsg2))
print("msg1, decrypted: " + t6.decrypt(encryptedMsg1, "123456789123456789123456"))
print("msg2, decrypted: " + t6.decrypt(encryptedMsg2, "CLE PLUS LONGUE , mais toujours dans la limite"))





