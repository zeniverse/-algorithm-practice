
def solution(rank, attendance):
    arr = []
    for idx, num in enumerate(rank):
        if attendance[idx]:
            arr.append((num, idx))

    arr.sort()
    
    return 10000 * arr[0][1] + 100 * arr[1][1] + arr[2][1]
        
rank = [3, 7, 2, 5, 4, 6, 1]
attendance = [False, True, True, True, True, False, False]
print(solution(rank, attendance))