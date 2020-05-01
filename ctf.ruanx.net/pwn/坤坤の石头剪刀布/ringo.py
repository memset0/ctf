import pwn
import random


def solve():
    counter = 0
    while True:
        server = pwn.remote('139.9.203.33', 30003)
        server.recvuntil('Input your choice>')
        seeds = list(range(0, 23333))
        counter = counter + 1
        while True:
            output = seeds[random.randint(0, len(seeds) - 1)] % 3
            if output == 0:
                server.sendline('1')
            elif output == 1:
                server.sendline('2')
            else:
                server.sendline('0')
            res = str(server.recvlines(1))
            print('output=', output, 'length=', len(seeds),
                  'counter=', counter)
            # print(seeds)

            if not 'nice try' in res:
                break
            if '(100/100)' in res:
                print(res)
                print(str(server.recvlines(1)))
                print(str(server.recvlines(1)))
                print(str(server.recvlines(1)))
                return

            next_seeds = set()
            for seed in seeds:
                if seed % 3 == output:
                    next_seeds.add((seed * seed + 233) % 23333)
            seeds = list(next_seeds)


solve()
