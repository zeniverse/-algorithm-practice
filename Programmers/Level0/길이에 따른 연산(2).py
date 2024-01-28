from functools import reduce

def solution(num_list):
    if len(num_list) >= 11:
        return sum(num_list)
    else:
        return eval('*'.join(list(map(str, num_list))))

num_list = [3, 4, 5, 2, 5, 4, 6, 7, 3, 7, 2, 2, 1]
print(solution(num_list))