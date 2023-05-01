
def solution(n):
    arr = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                arr[i].append(1)
            else:
                arr[i].append(0)
    return arr

n = 6
print(solution(n))