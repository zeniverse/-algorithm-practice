
def solution(l, r):
    res = []
    for num in range(l, r + 1):
        if not set(str(num)) - set(["0", "5"]):
            res.append(num)
    return res or [-1]
        
l, r = 5, 555
print(solution(l, r))