from collections import Counter

arr = list(map(int, input().split()))
val = Counter(arr).most_common()

if val[0][1] == 3:
    print(10000 + int(val[0][0]) * 1000)
elif val[0][1] == 2:
    print(1000 + int(val[0][0]) * 100)
else:
    print(int(max(arr)) * 100)