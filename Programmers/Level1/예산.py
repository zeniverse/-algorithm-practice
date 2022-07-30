
d = [1,3,2,5,4]
budget = 9

res = 0

d.sort()

for i in d:
    if budget - i >= 0:
        budget -= i
        res += 1
    else:
        break

print(res)

