from math import gcd

denum1, num1, denum2, num2 = 9, 2, 1, 3

def solution(denum1, num1, denum2, num2):

    denum = (denum1 * num2) + (denum2 * num1)
    num = num1 * num2

    gcd_ = gcd(denum, num)

    return [denum // gcd_, num // gcd_]
    

print(solution(denum1, num1, denum2, num2))
