from math import gcd

denum1, num1, denum2, num2 = 9, 2, 1, 3

def solution(denum1, num1, denum2, num2):
    res = []

    parent = (num1 * num2) // gcd(num1, num2)
    mul1 = parent // num1
    mul2 = parent // num2

    denum1 *= mul1
    denum2 *= mul2

    res.append((denum1 + denum2) // gcd((denum1 + denum2), parent))
    res.append(parent // gcd((denum1 + denum2), parent))

    return res
    

print(solution(denum1, num1, denum2, num2))
