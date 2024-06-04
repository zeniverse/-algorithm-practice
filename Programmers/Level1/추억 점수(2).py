
def solution(name, yearning, photo):
    dic = dict(zip(name, yearning))
    res = []

    for p in photo:
        tmp = 0
        for n in p:
            if n in dic:
                tmp += dic[n]
        res.append(tmp)

    return res

name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]

print(solution(name, yearning, photo))

