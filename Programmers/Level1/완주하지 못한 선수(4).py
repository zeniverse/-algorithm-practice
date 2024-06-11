from collections import defaultdict

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]	

def solution(participant, completion):
    dic = defaultdict(int)
    
    for i in participant:
        dic[i] += 1
    
    for i in completion:
        dic[i] -= 1
        
    for v, k in dic.items():
        if k != 0:
            return v

print(solution(participant, completion))
