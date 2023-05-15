
def solution(str_list):
    str = ''.join(str_list)
    index_l = str.find("l")
    index_r = str.find("r")

    if (index_l < index_r and index_l != -1) or (index_r == -1 and index_l != -1):
        return str_list[:index_l]
    elif (index_r < index_l and index_r != -1) or (index_l == -1 and index_r != -1):
        return str_list[index_r + 1:]
    else:
        return []

str_list = ["u", "l", "d"]
print(solution(str_list))