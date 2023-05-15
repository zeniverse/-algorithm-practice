
def solution(picture, k):
    res = []
    for str in picture:
        tmp = ''
        for i in str:
            tmp += i * k
        for j in range(k):
            res.append(tmp)
    return res
        
picture = [".xx...xx.", "x..x.x..x", "x...x...x", ".x.....x.", "..x...x..", "...x.x...", "....x...."]
k = 2
print(solution(picture, k))