

s = '{{2},{2,1},{2,1,3},{2,1,3,4}}'


res = []

s = s[:-2].replace('{', '').replace(',', ' ').split('}')
s = [i.split() for i in s]

print(s)

s.sort(key=lambda x: len(x))
print(s)

for tup in s:
    diff = set(tup) - set(res)
    res.append(list(diff)[0])

res = [int(i) for i in res]
print(res)
    
