'''resum frase'''
from Crypto.Hash import SHA256

MISSATGE = input("frase: ")

OBJH = SHA256.new(MISSATGE.ENCODE('utf-8'))
RESUM = OBJH.HEXDIGEST()


print(RESUM)

RESUM = str(RESUM)
ARCHI = open('resum.txt', 'w')
ARCHI.write(RESUM)
ARCHI.close()

