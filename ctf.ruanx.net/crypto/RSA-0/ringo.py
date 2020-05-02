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


def encrypt(m, N, e):           # 加密
    return pow(m, e, N)


def decrypt(c, N, d):           # 解密
    return pow(c, d, N)


def old_solve():
    # 拿 bsdgames 里面的 `primes` 程序随便造的 p, q
    p = 100088459
    q = 1000049473

    N = p * q
    phi = (p - 1) * (q - 1)
    e = 2333333
    d = getInv(e, phi)

    c = encrypt(123454321, N, e)
    print(c)  # 加密 `123454321`，得到密文：`8922052926595796`

    m = decrypt(c, N, d)
    print(m)  # 解密，得到明文 `123454321`


def solve():
    p = 190200647956112783535765008317161963047
    q = 285665635359057201725659119374017317427
    N = p * q
    phi = (p - 1) * (q - 1)

    e = 65537
    d = getInv(e, phi)

    c = 2404704211304008728001190278809748948299133006732012442286327326548630531233
    m = decrypt(c, N, d)
    print(m)


# old_solve()
solve()
