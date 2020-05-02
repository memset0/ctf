from Crypto.Cipher import AES
from secret import flag
import time
from hashlib import md5
import base64

key = md5(str(int(time.time())).encode()).digest()
aes = AES.new(key, AES.MODE_ECB)
outData = aes.encrypt(flag.encode('utf-8'))

with open('flag.enc', 'wb') as f:
    f.write(base64.b64encode(outData))
