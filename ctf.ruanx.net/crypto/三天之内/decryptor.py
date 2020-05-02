from Crypto.Cipher import AES
from secret import flag
import time
from hashlib import md5
import base64

with open('flag.enc', 'rb') as f:
    encoded_flag = base64.b64decode(f.read())

magic_clock = 1588441382
start_clock = magic_clock - 0 * 24 * 60 * 60
end_clock = start_clock - 10 * 24 * 60 * 60
for clock in range(start_clock, end_clock, -1):
    key = md5(str(clock).encode()).digest()
    aes = AES.new(key, AES.MODE_ECB)
    flag = aes.decrypt(encoded_flag)
    # if clock % 3600 == 0:
    #     print(clock, flag)
    try:
        print(clock, flag, flag.decode())
    except:
        continue