
numlist = [10000,20,36,47,40,6,10,7000]
n = 30

def solution(numlist, n):
    return sorted(numlist, key=lambda x:(abs(x - n), -x))

print(solution(numlist, n))