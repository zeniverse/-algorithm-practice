from functools import cmp_to_key

def compare(x, y):
    if str(y) + str(x) >= str(x) + str(y):
        return 1
    else:
        return -1
    
    # return 음수 : 먼저 들어온 요소가 앞으로 정렬
    # return 0 :  바뀌지 않음
    # return 양수 : 나중에 들어온 요소가 앞으로 정렬

def solution(numbers):
    numbers = sorted(numbers, key = cmp_to_key(compare))
    return str(int("".join(map(str,numbers))))

numbers = [6, 10, 2]
print(solution(numbers))