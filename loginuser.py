'''crear login'''
from Crypto.Hash import SHA256
US = input("Usuari: ")

PWD = input("Contraseña: ")

OBJH = SHA256.new(PWD.ENCODE('utf-8'))
RESUM = OBJH.HEXDIGEST()
print(RESUM)


ARCHI = open('archivologin.txt', 'w')
ARCHI.write(US + ':' + RESUM)
ARCHI.close()

