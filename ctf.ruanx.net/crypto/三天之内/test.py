from Crypto.Cipher import AES
import base64

key = bytes('this_is_a_key'.ljust(16,' '),encoding='utf8')
aes = AES.new(key,AES.MODE_ECB)

# encrypt
plain_text = bytes('this_is_a_plain'.ljust(16,' '),encoding='utf8')
text_enc = aes.encrypt(plain_text)
text_enc_b64 = base64.b64encode(text_enc)
print(text_enc_b64.decode(encoding='utf8'))

# decrypt
msg_enc = base64.b64decode(text_enc_b64)
msg = aes.decrypt(msg_enc)
print(msg.decode(encoding='utf8'))