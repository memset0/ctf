p = 252647779892687905173761792949656998433
q = 290615416181922737045361451171930371659
r = 281613259213037257262703439109757908501

flag = 123456

n = p * q * r
e = 0x10001
print(pow(flag, e, n))
# 1169612223485519024207841670191078798101684935551461601922416127588930439758194701318838707953651437973827125265577