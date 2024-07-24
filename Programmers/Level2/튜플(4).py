import re
from collections import Counter

s = '{{1,2,3},{2,1},{1,2,4,3},{2}}'

def solution(s):
    s = Counter(re.findall('\d+', s))
    return list(map(int,[k for k, v in sorted(s.items(), key=lambda x:x[1], reverse=True)]))

print(solution(s))

