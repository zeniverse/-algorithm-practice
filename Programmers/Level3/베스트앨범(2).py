

def solution(genres, plays):
    res = []
    dict = {e:[] for e in set(genres)}

    for g, p, idx in zip(genres, plays, range(len(genres))):
        dict[g].append((p, idx))

    print(dict)

    for k, v in dict.items():
        v = sorted(v, key= lambda x: -x[0])
        total  = sum([i[0] for i in v])
        
        for i in range(min(len(v), 2)):
            res.append((total, v[i][1]))

    print(res)
    
    return [i[1] for i in sorted(res, key=lambda x:-x[0])]

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))
