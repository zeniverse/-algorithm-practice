
my_str = "abc1Addfggg4556b"
n = 6

def solution(my_str, n):
    res = []
    idx = 0

    while idx < len(my_str):
        idx += n
        res.append(my_str[idx - n : idx])
        

    if idx <= len(my_str) - 1:
        res.append(my_str[idx:])

    return res


print(solution(my_str, n))
