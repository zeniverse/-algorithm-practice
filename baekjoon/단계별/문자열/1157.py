from collections import Counter

s = list(input().upper())
val = Counter(s).most_common()

if len(val) >= 2 and val[0][1] == val[1][1]:
    print("?")
else:
    print(val[0][0])