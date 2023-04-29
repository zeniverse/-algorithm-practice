
def solution(num_list):
    return max(sum(num_list[0:len(num_list):2]), sum(num_list[1:len(num_list) : 2]))

num_list = [4, 2, 6, 1, 7, 6]
print(solution(num_list))