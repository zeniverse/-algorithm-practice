s = input().replace(" ", "")
res = 'UCPC'
idx = 0

for i in s:
    if i == res[idx]:
        idx += 1
    if idx == 4:
        print("I love UCPC")
        break
else:
    print("I hate UCPC")