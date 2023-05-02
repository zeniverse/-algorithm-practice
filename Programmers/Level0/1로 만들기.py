
def solution(num_list):
    res = 0

    for num in num_list:
        while num != 1:
            if num % 2:
                num = (num - 1) // 2
            else:
                num //= 2
            res += 1
    return res

num_list = [12, 4, 15, 1, 14]
print(solution(num_list))