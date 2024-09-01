
def change(n, k):
    res = ""

    while n > 0:
        n, mod = divmod(n, k)
        res += mod
    return res[::-1]

def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    number = change(n, k)
    
    for i in list(number.split("0")):
        if i != "":
            if is_prime(int(i)):
                answer += 1
    
    return answer

n, l, r = 2, 4, 17
print(solution(n, l, r))