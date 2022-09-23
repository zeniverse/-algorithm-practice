
queue1 = [3, 2, 7, 2]
queue2 = [4, 6, 5, 1]

def solution(queue1, queue2):

    arr = queue1 + queue2
    target = sum(arr) // 2

    i = 0
    j = len(queue1) - 1
    current = sum(queue1)
    count = 0

    while i < len(arr) and j < len(arr):
        if current == target:
            return count

        if current < target and j < len(arr) - 1:
            j += 1
            current += arr[j]
        else:
            current -= arr[i]
            i += 1

        count += 1

    return -1

print(solution(queue1, queue2))
