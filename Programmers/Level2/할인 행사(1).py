
want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]

def solution(want, number, discount):
    res = 0

    for i in range(len(discount)):
        tmp = discount[i:i + 10]
        flag = False
        for j in range(len(want)):
            dis = tmp.count(want[j])
            if dis >= number[j]:
                flag = True
            else:
                flag = False
                break
        if flag:
            res += 1

    return res

print(solution(want, number, discount))