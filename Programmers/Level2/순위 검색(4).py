from collections import defaultdict
from bisect import bisect_left

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

def solution(info, query):
    answer = []
    arr = defaultdict(list)

    for i in info:
        tmp = i.split()

        for l in [tmp[0], '-']:
            for j in [tmp[1], '-']:
                for c in [tmp[2], '-']:
                    for f in [tmp[3], '-']:
                        arr[l+j+c+f].append(int(tmp[4]))

    for key in arr:
        arr[key].sort()

    for q in query:
        q = q.replace("and ","").split()

        score = int(q[-1])
        s = "".join(q[:-1])

        left = bisect_left(arr[s], score)
        answer.append(len(arr[s]) - left)

    return answer

print(solution(info, query))