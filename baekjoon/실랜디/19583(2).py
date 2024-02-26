from collections import defaultdict
from datetime import datetime
import sys
input = sys.stdin.readline

s, e, q = input().rstrip().split()
s, e, q = datetime.strptime(s, "%H:%M"), datetime.strptime(e, "%H:%M"), datetime.strptime(q, "%H:%M")
dic = defaultdict(list)
res = 0

while True:
    try:
        time, name = input().rstrip().split()
        tmp = datetime.strptime(time, "%H:%M")
        if tmp <= s:
            dic[name].append(('s', time))
        elif e <= tmp <= q:
            dic[name].append(('e', time))
    except:
        break

for name, times in dic.items():
    if len(times) >= 2:
        flag = False
        for check, t in times:
            if check == 's':
                flag = True
            elif check == 'e' and flag:
                res += 1
                break
            
print(res)
