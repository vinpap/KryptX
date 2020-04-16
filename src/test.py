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

print("CAESAR CIPHER")
encryptedMsg1 = t1.encrypt(msg1, 7)
encryptedMsg2 = t1.encrypt(msg2, 4)
print("msg1, encrypted: " + str(encryptedMsg1))
print("msg2, encrypted: " + str(encryptedMsg2))
print("msg1, decrypted: " + t1.decrypt(encryptedMsg1, 7))
print("msg2, decrypted: " + t1.decrypt(encryptedMsg2, 4))

print("VIGENÈRE CIPHER")
encryptedMsg1 = t2.encrypt(msg1, "PATATE")
encryptedMsg2 = t2.encrypt(msg2, "CONCOMBRE")
print("msg1, encrypted: " + str(encryptedMsg1))
print("msg2, encrypted: " + str(encryptedMsg2))
print("msg1, decrypted: " + t2.decrypt(encryptedMsg1, "PATATE"))
print("msg2, decrypted: " + t2.decrypt(encryptedMsg2, "CONCOMBRE"))

print("ENIGMA M3")
settings = [('f', 'k', 'z'),
            (4, 1, 2),
            ('z', 'b', 'f'),
            [('a', 'h'), ('b', 'i'), ('c', 'j'), ('d', 'k'), ('e', 'l'), ('f', 'm'), ('g', 'n'), ('o', 'z'), ('p', 'y'), ('q', 'x')]]
encryptedMsg1 = t3.encrypt(msg1, settings)
encryptedMsg2 = t3.encrypt(msg2, settings)
print("msg1, encrypted: " + str(encryptedMsg1))
print("msg2, encrypted: " + str(encryptedMsg2))
print("msg1, decrypted: " + t3.decrypt(encryptedMsg1, settings))
print("msg2, decrypted: " + t3.decrypt(encryptedMsg2, settings))

print("DES")
encryptedMsg1 = t4.encrypt(msg1, "KEYKEYKE")
encryptedMsg2 = t4.encrypt(msg2, "CLE PLUS LONGUE ")
print("msg1, encrypted: " + str(encryptedMsg1))
print("msg2, encrypted: " + str(encryptedMsg2))
print("msg1, decrypted: " + t4.decrypt(encryptedMsg1, "KEYKEYKE"))
print("msg2, decrypted: " + t4.decrypt(encryptedMsg2, "CLE PLUS LONGUE "))

print("AES")
encryptedMsg1 = t5.encrypt(msg1, "123456789123456789123456")
encryptedMsg2 = t5.encrypt(msg2, "CLE PLUS LONGUE ")
print("msg1, encrypted: " + str(encryptedMsg1))
print("msg2, encrypted: " + str(encryptedMsg2))
print("msg1, decrypted: " + t5.decrypt(encryptedMsg1, "123456789123456789123456"))
print("msg2, decrypted: " + t5.decrypt(encryptedMsg2, "CLE PLUS LONGUE "))

print ("BLOWFISH")
encryptedMsg1 = t6.encrypt(msg1, "123456789123456789123456")
encryptedMsg2 = t6.encrypt(msg2, "clé encodée en utf-8")
print("msg1, encrypted: " + str(encryptedMsg1))
print("msg2, encrypted: " + str(encryptedMsg2))
print("msg1, decrypted: " + t6.decrypt(encryptedMsg1, "123456789123456789123456"))
print("msg2, decrypted: " + t6.decrypt(encryptedMsg2, "clé encodée en utf-8"))

print("RSA")
keys1 = t7.generateKeysPair()
keys2 = t7.generateKeysPair()
encryptedMsg1 = t7.encrypt(msg1, keys1[1])
encryptedMsg2 = t7.encrypt(msg2, keys2[1])
print("msg1, encrypted: " + str(encryptedMsg1))
print("msg2, encrypted: " + str(encryptedMsg2))
print("msg1, decrypted: " + t7.decrypt(encryptedMsg1, keys1[0]))
print("msg2, decrypted: " + t7.decrypt(encryptedMsg2, keys2[0]))

print("MD5")
hashedMsg1 = t8.encrypt(msg1)
hashedMsg2 = t8.encrypt(msg2)
print("msg1, hashed: " + str(hashedMsg1))
print("msg2, hashed: " + str(hashedMsg2))

print("SHA")
hashedMsg1 = t9.encrypt(msg1)
hashedMsg2 = t9.encrypt(msg2)
print("msg1, hashed: " + str(hashedMsg1))
print("msg2, hashed: " + str(hashedMsg2))



