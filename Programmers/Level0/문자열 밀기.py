
A = "apple"
B = "elppa"

def solution(A, B):
    a = list(A)

    for i in range(len(A) - 1):
        A = A[-1] + A[:len(A) - 1]
        if A == B:
            return i
    return -1

print(solution(A, B))
