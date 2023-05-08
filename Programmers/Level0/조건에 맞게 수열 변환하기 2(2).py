def solution(arr):
    res = 0
    old = arr
    while True:
        new = []
        
        for i in old:
            if i >= 50 and i % 2 == 0:
                i = i/2
            elif i < 50 and i % 2:
                i = i * 2 + 1
            new.append(i)
        
        if old == new:
            return res
        else:
            old = new
            res += 1
            

arr = [1, 2, 3, 100, 99, 98]
print(solution(arr))