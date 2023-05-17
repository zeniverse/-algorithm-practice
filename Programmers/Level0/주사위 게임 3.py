
def solution(a, b, c, d):
    arr = [a, b, c, d]
    counts = [arr.count(i) for i in arr]

    if max(counts) == 4:
        return 1111 * a
    elif max(counts) == 3:
        p = arr[counts.index(3)]
        q = arr[counts.index(1)]

        return (10 * p + q) ** 2
    elif max(counts) == 2:
        if min(counts) == 2:
            return (a + c) * abs(a - c) if a == b else (a + b) * abs(a - b)
        else:
            p = arr[counts.index(2)]
            return (a * b * c * d) / p**2
    else:
        return min(arr)

    
        
a, b, c, d = 2, 2, 2, 2
print(solution(a, b, c, d))