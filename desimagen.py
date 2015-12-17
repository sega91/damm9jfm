'''desincriptar imatge'''
from Crypto.Cipher import AES
CLAU = "?6gNvS4j3/!CXe77".encode('utf-8')
IV = "pcb34y27pcb34y27".encode('utf-8')
OBJ = AES.new(CLAU, AES.MODE_CBC, IV)


FILE_ENC = open("img.enc", "rb")
FILE_DES = open("imgdesc.jpg", "wb")
BLOCS = 8192
while True:
    BLOC = FILE_ENC.read(BLOCS)
    if not BLOC:
        break
    NUM = len(BLOC)
    MOD = NUM % 16
    if MOD > 0:
        PADDING = 16 - MOD
        BLOC = b"0" * PADDING
    CODIFICAT = OBJ.DECRYPT(BLOC)
    FILE_DES.write(CODIFICAT)
FILE_DES.close()
FILE_ENC.close()
