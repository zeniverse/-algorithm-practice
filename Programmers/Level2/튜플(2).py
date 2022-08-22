s = '{{2},{2,1},{2,1,3},{2,1,3,4}}'


res = []

s = s.lstrip('{').rstrip('}').split('},{')
s = [i.split(',') for i in s]

print(s)
s.sort(key=len)

for tup in s:
    diff = set(tup) - set(res)
    res.append(list(diff)[0])

print([int(i) for i in res])

