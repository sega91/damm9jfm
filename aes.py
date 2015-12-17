''' AES '''
from Crypto.Cipher import AES
CLAU = b"?6gNvS4j3/!CXe77"
IV = "pcb34y27pcb34y27"
OBJ = AES.new(CLAU, AES.MODE_CBC, IV)

MISSATGE = b"mensaje incripta"

CODIFICAT = OBJ.ENCRYPT(MISSATGE)

print("Missatge original:", MISSATGE)
print("Missatge codificat:", CODIFICAT)

OBJ2 = AES.new(CLAU, AES.MODE_CBC, IV)
DECO = OBJ2.DECRYPT(CODIFICAT)
print("Missatge descodificat:", DECO)
