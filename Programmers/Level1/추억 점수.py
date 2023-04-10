from collections import defaultdict

def solution(name, yearning, photo):
    res = []
    dic = defaultdict(int)
    
    for n, y in zip(name, yearning):
        dic[n] = y

    for people in photo:
        cnt = 0
        for person in people:
            cnt += dic[person]
        res.append(cnt)

    return res

name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]

print(solution(name, yearning, photo))

