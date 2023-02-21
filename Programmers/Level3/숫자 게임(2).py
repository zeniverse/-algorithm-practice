

def solution(A, B):
    res = 0

    A.sort()
    B.sort()

    ai, bi = 0, 0

    while ai != len(A) and bi != len(B):
        if B[bi] > A[ai]:
            res += 1
            ai += 1
            bi += 1
        else:
            bi += 1
    
    return res

A = [5,1,3,7]
B = [2,2,6,8]

print(solution(A, B))
