import base64

def caesar_decrypt(m, k):
    r = ""
    for i in m:
        r += chr((ord(i) - k) % 128)
    return r

# b = 'bXNobgJyaHB6aHRwdGgE'
b = 'OD4zOU1GN0VGTw=='

a = base64.b64decode(b)
print(a)
print(a.decode())
for k in range(128):
	print(caesar_decrypt(a.decode(), k))