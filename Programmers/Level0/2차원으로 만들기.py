
num_list = [100, 95, 2, 4, 5, 6, 18, 33, 948]
n = 3

def solution(num_list, n):
    res = []
    tmp = []

    for i in range(1, len(num_list) + 1):
        tmp.append(num_list[i - 1])

        if i % n == 0:
            res.append(tmp)
            tmp = []
        
    return res

print(solution(num_list, n))
