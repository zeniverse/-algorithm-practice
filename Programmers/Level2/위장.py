from collections import defaultdict


clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

arr = defaultdict(list)
res = 1

for i in clothes:
    arr[i[1]].append(i[0])

for key in arr.keys():
    res *= len(arr[key]) + 1

res -= 1

print(res)