
dots = [[-1, -1], [1, 1], [1, -1], [-1, 1]]

def distance(arr1, arr2):
    return abs(arr1[0] - arr2[0]) + abs(arr1[1]-arr2[1])

def solution(dots):
    dots.sort()
    width = distance(dots[0], dots[2])
    height = distance(dots[0], dots[1])

    return width * height


print(solution(dots))
