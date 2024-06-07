
k, score = 4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]

def solution(k, score):
    res = []
    q = []

    for s in score:
        q.append(s)

        if len(q) > k :
            q.remove(min(q))
        
        res.append(min(q))

    return res
    

print(solution(k, score))