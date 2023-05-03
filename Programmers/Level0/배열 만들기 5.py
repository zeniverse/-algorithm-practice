
def solution(intStrs, k, s, l):
    res = []

    for i in intStrs:
        num = int(i[s:s+l])
        if num > k:
            res.append(num)
    return res

intStrs = ["0123456789","9876543210","9999999999999"]
k = 50000
s, l = 5, 5
print(solution(intStrs, k, s, l))