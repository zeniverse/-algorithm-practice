
A = [1, 4, 2]
B = [5, 4, 4]

def solution(A, B):
    return sum(a * b for a, b in zip(sorted(A), sorted(B, reverse=True)))

print(solution(A, B))