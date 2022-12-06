
A = "hello"
B = "ohell"

def solution(A, B):
    AA = A + A

    res = AA.find(B)

    if res > 0:
        res = len(A) - res

    return res

print(solution(A, B))
