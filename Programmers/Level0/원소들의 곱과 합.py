from functools import reduce

def solution(num_list):
    s = sum(num_list)
    m = reduce(lambda x, y : x * y, num_list)

    return 1 if s**2 > m else 0
    

num_list = [3, 4, 5, 2, 1]
print(solution(num_list))