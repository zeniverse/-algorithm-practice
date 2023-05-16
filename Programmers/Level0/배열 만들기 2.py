
def solution(l, r):
    res = []
    for i in range(l, r + 1):
        flag = True
        for j in str(i):
            if j not in ["5", "0"]:
                flag = False
                break
        if flag:
            res.append(i)
    return res or [-1]
        
l, r = 5, 555
print(solution(l, r))