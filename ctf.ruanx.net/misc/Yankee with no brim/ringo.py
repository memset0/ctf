import os
import binascii
import struct


misc = open("yankee_with_brim.png", "rb").read()

for i in range(2048):
	for j in range(2048):
			data = misc[12:16] + struct.pack('>i', i) + struct.pack('>i', j) + misc[24:29]
			crc32 = binascii.crc32(data) & 0xffffffff
			if crc32 == 0xbe6698dc:
					print(i, j)

# print(0x00000258)
# print(0x000001f4)