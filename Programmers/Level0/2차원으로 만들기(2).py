
num_list = [100, 95, 2, 4, 5, 6, 18, 33, 948]
n = 3

def solution(num_list, n):
    res = []

    for i in range(0, len(num_list), n):
        res.append(num_list[i : i + n])
        
    return res

print(solution(num_list, n))
