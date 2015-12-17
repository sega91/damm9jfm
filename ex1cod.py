'''ex1cod'''
from Crypto.Cipher import AES
CLAU = b"?6gNvS4j3/!CXe77"
IV = "pcb34y27pcb34y27"
OBJ = AES.new(CLAU, AES.MODE_CBC, IV)


MISSATGE = input("Introduir misatge ")
NUM = len(MISSATGE)
MOD = NUM % 16

if MOD > 0:
    PADDING = 16 - MOD
    MISSATGE = "0" * PADDING

CODIFICAT = OBJ.ENCRYPT(MISSATGE)

print("Missatge original:", MISSATGE[:NUM])
print("Missatge codificat:", CODIFICAT)

OBJ2 = AES.new(CLAU, AES.MODE_CBC, IV)
DECO = OBJ2.DECRYPT(CODIFICAT)
print("Missatge descodificat:", DECO[:NUM])
