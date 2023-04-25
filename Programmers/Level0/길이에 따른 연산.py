from functools import reduce

def solution(num_list):
    if len(num_list) <= 10:
        return reduce(lambda x, y: x * y, num_list)
    else:
        return sum(num_list)

num_list = [3, 4, 5, 2, 5, 4, 6, 7, 3, 7, 2, 2, 1]
print(solution(num_list))