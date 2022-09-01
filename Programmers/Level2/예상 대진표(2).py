

n = 8
a = 2
b = 3

def solution(n, a, b):

    count = 0

    while a != b:
        count += 1

        a = (a + 1)//2
        b = (b + 1)//2
        
    return count

print(solution(n, a, b))

