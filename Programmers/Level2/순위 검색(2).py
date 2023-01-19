from collections import defaultdict
from itertools import combinations
from bisect import bisect_left

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

def solution(info, query):
    res = []
    info_dict = defaultdict(list)

    for i in range(len(info)):
        tmp = info[i].split()
        myKey = tmp[:-1]
        myVal = int(tmp[-1])

        for j in range(5):
            for combi in combinations(myKey, j):
                key = ''.join(combi)
                info_dict[key].append(myVal)

    for i in info_dict:
        info_dict[i].sort()

    print(info_dict)

    for q in query:
        tmp = q.replace('and', '').split()
    
        query_key = ''.join(tmp[:-1]).replace("-", "")
        query_val = int(tmp[-1])
        
        if query_key in info_dict:
            scores = info_dict[query_key]
            enter = bisect_left(scores, query_val)

            res.append(len(scores) - enter)
        else:
            res.append(0)

    return res

print(solution(info, query))