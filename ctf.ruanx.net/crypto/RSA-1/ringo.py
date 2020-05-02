def exgcd(a, b):                   # 扩展欧几里得算法
    if b == 0:
        return (1, 0)
    x, y = exgcd(b, a % b)
    # print('exgcd', a, b, x, y)
    return (y, x - a // b * y)


def getInv(a, mod):                # exgcd求逆元
    x, y = exgcd(a, mod)
    return x % mod
    # Python下负数模正数得到正数。如果是其他语言，得返回 (x % mod + mod) % mod


def encrypt(m, n, e):           # 加密
    return pow(m, e, n)


def decrypt(c, n, d):           # 解密
    return pow(c, d, n)


def old_solve():
    # 拿 bsdgames 里面的 `primes` 程序随便造的 p, q
    p = 100088459
    q = 1000049473

    n = p * q
    phi = (p - 1) * (q - 1)
    e = 2333333
    d = getInv(e, phi)

    c = encrypt(123454321, n, e)
    print(c)  # 加密 `123454321`，得到密文：`8922052926595796`

    m = decrypt(c, n, d)
    print(m)  # 解密，得到明文 `123454321`


def solve():
    p = 252647779892687905173761792949656998433
    q = 290615416181922737045361451171930371659
    r = 281613259213037257262703439109757908501
    n = p * q * r
    phi = (p - 1) * (q - 1) * (r - 1)

    e = 0x10001
    d = getInv(e, phi)

    c = 1169612223485519024207841670191078798101684935551461601922416127588930439758194701318838707953651437973827125265577
    m = decrypt(c, n, d)
    print(m)


# old_solve()
solve()
