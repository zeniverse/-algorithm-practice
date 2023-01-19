
info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

def solution(info, query):
    res = []
    data = dict()
    
    for a in ['cpp', 'java', 'python', '-']:
        for b in ['backend', 'frontend', '-']:
            for c in ['junior', 'senior', '-']:
                for d in ['chicken', 'pizza', '-']:
                    data.setdefault((a, b, c, d), list())

    for i in info:
        i = i.split()
        for a in [i[0], '-']:
            for b in [i[1], '-']:
                for c in [i[2], '-']:
                    for d in [i[3], '-']:
                        data[(a, b, c, d)].append(int(i[-1]))

    print(data)

    for i in data:
        data[i].sort()

    for q in query:
        q = q.split()
        
        scores = data[(q[0], q[2], q[4], q[6])]
        find = int(q[7])

        start = 0
        end = len(scores)
        mid = 0

        while start < end:
            mid = (start + end) // 2

            if scores[mid] >= find:
                end = mid
            else:
                start = mid + 1

        res.append(len(scores) - start)

    return res

print(solution(info, query))