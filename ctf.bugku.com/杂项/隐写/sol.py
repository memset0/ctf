import os
import pwn
import struct
import binascii


misc = open("2.png", "rb").read()

# for i in range(2048):
# 	for j in range(2048):
# 			data = misc[12:16] + struct.pack('>i', i) + struct.pack('>i', j) + misc[24:29]
# 			crc32 = binascii.crc32(data) & 0xffffffff
# 			if crc32 == 0xcbd6df8a:
# 					print(i, j)

print(pwn.p64(500))