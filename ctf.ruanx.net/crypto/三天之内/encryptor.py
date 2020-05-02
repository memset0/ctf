from Crypto.Cipher import AES
import os
import time
# from secret import flag
from hashlib import md5
import base64

flag = '123456'
# key = md5(str(int(time.time())).encode()).digest()
key = os.urandom(16)
aes = AES.new(key, AES.MODE_ECB)
outData = aes.encrypt(flag)
# print(str(outData))

with open('flag.enc', 'wb') as f:
    f.write(base64.b64encode(outData))
