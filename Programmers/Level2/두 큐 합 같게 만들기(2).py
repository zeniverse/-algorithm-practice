
queue1 = [3, 2, 7, 2]
queue2 = [4, 6, 5, 1]

def solution(queue1, queue2):

    arr = queue1 + queue2

    if sum(arr) % 2 == 1:
        return -1
    
    queue1_sum = sum(queue1)
    target = sum(arr) // 2
    start = 0
    end = len(queue1)
    count = 0

    while start <= end and end < len(arr):
        if queue1_sum == target:
            return count
        
        if queue1_sum < target:
            queue1_sum += arr[end]
            end += 1
        else:
            queue1_sum -= arr[start]
            start += 1

        count += 1
    return -1

print(solution(queue1, queue2))
