
def solution(num_list):
    num_list = sorted(num_list)
    return num_list[5:]

num_list = [12, 4, 15, 46, 38, 1, 14, 56, 32, 10]
print(solution(num_list))