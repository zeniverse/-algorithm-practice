from collections import deque

A = "hello"
B = "ohell"

def solution(A, B):
    a, b = deque(A), deque(B)

    for count in range(0, len(A)):
        if a == b:
            return count
        a.rotate(1)

    return -1

print(solution(A, B))
