from collections import Counter

want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]

def solution(want, number, discount):
    res = 0
    dic = {}

    for i in range(len(want)):
        dic[want[i]] = number[i]

    for i in range(len(discount) - 9):
        if dic == Counter(discount[i:i + 10]):
            print(Counter(discount[i:i + 10]))
            res += 1
    
    return res

print(solution(want, number, discount))