
from collections import defaultdict
import math

def solution(fees, records):
    answer = []
    dic = defaultdict(list)
    
    for record in records:
        a, b, c  = record.split(" ")
        t, m = map(int, a.split(":"))
        dic[b].append(t * 60 + m)
        
    for k, v in dic.items():
        if len(v) % 2 == 1:
            v.append(23*60 + 59)
        time = 0
        for i in range(1, len(v), 2):
            time += (v[i] - v[i - 1])
        
        if time > fees[0]:
            time -= fees[0]
        else:
            time = 0
        answer.append((k, fees[1] + (math.ceil(time / fees[2]) * fees[3])))
        
    answer.sort()
    return [i[1] for i in answer]

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees, records))