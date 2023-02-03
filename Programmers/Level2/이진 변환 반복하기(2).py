
def solution(s):
    res = [0, 0]

    while s != '1':
        zero = s.count("0")
        res[0] += 1
        res[1] += zero

        s = s.replace("0", "")
        s = bin(len(s))[2:]

    return res
        

s = "1111111"
print(solution(s))

