from collections import defaultdict

friends = ["muzi", "ryan", "frodo", "neo"]
gifts = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]


def solution(friends, gifts):
    dic = defaultdict(list)
    dic_count = defaultdict(int)
    res = defaultdict(int)
    
    for i in gifts:
        a, b = i.split()
        dic[a].append(b)
        dic_count[a] += 1
        dic_count[b] -= 1
        
    for i in range(len(friends)):
        for j in range(i + 1, len(friends)):
            a = dic[friends[i]].count(friends[j])
            b = dic[friends[j]].count(friends[i])
            
            if a > b:
                res[friends[i]] += 1
            elif a < b:
                res[friends[j]] += 1
            elif a == b:
                if dic_count[friends[i]] > dic_count[friends[j]]:
                    res[friends[i]] += 1
                elif dic_count[friends[i]] < dic_count[friends[j]]:
                    res[friends[j]] += 1 

    return 0 if not res else max(res.values())

print(solution(friends, gifts))
    