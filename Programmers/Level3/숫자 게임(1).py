

def solution(A, B):
    res = 0

    A.sort()
    B.sort()

    j = 0

    for i in range(len(A)):
        if A[j] < B[i]:
            res += 1
            j += 1
    
    return res

A = [5,1,3,7]
B = [2,2,6,8]

print(solution(A, B))
