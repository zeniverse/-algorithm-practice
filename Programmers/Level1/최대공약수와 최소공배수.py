def gcd(a, b):

    if a < b:
        a, b, = b, a

    if b == 0:
        return a
    return gcd(b, a%b)

n = 2
m = 5

print([gcd(n, m), (n * m)//gcd(n, m)])