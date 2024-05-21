
dots = [[1, 4], [9, 2], [3, 8], [11, 6]]

def gradient(a, b):
    return (a[1] - b[1]) / (a[0] - b[0])

def solution(dots):
    if gradient(dots[2], dots[0]) == gradient(dots[3], dots[1]) or gradient(dots[3], dots[2]) == gradient(dots[1], dots[0]):
        return 1
    else:
        return 0
    
print(solution(dots))