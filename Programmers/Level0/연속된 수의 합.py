
num = 3
total = 12

def solution(num, total):
    answer = []
    temp = 0

    if num % 2 == 0:
        temp = int(total//num) - int(num//2 - 1)
        answer = list(range(temp,num+temp))
    else:
        temp = int(total//num) - int(num//2)
        answer = list(range(temp,num+temp))

    return answer



print(solution(num, total))
