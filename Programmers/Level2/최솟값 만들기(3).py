
def solution(A, B):
    
    return sum(map(lambda a, b : a * b, sorted(A), sorted(B, reverse=True)))

A = [1, 4, 2]
B = [5, 4, 4]
print(solution(A, B))