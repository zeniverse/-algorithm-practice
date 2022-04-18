croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = input()
count = 0

for i in croatia:
    if i in s:
        s = s.replace(i, "1")

print(len(s))