
def climbStairs(n):
    if n <= 3:
        return n
    
    a, b = 1, 2

    for _ in range(3, n + 1):
        a, b = b, a + b

    return b

print(climbStairs(5))