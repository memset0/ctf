from Crypto.Cipher import AES
from secret import flag
import time
from hashlib import md5
import base64

ljusted_flag = bytes(flag.ljust(16,' '),encoding='utf8')
key = md5(str(int(time.time())).encode()).digest()
aes = AES.new(key, AES.MODE_ECB)
outData = aes.encrypt(ljusted_flag)
# print(str(int(time.time())))
# print(flag, ljusted_flag)
print(outData)

with open('flag.enc', 'wb') as f:
    f.write(base64.b64encode(outData))
    f.close()

with open('flag.enc', 'rb') as f:
    encoded_flag = base64.b64decode(f.read())
    flag = aes.decrypt(encoded_flag)
    print(encoded_flag)
    print(flag)