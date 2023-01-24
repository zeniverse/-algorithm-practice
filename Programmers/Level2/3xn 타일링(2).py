
n = 4

def solution(n):
    if n % 2:
        return 0

    front = back = 1
    for _ in range(n // 2):
        front, back = back, (back * 4 - front) % 1000000007
    
    return back

print(solution(n))