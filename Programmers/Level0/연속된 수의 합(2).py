
num = 3
total = 12

def solution(num, total):
    # 시작수를 start라고 할때 n항까지의 합은
    #  start, start + 1, start + 2, ... start + num - 1 이다 (마지막항에서 -1을 하는 이유는 앞에 start로 시작했기 때문)
    #  따라서 (num * start) + (1 + 2 + 3 + ... + num) (start가 num 개수 만큼 있으므로)
    
    number = sum(range(1, num))
    
    # 이미 1~num까지의 합은 구했으므로 total에서 number만큼 빼주기?
    start = (total - number) // num
    return [i for i in range(start, start + num)]



print(solution(num, total))
