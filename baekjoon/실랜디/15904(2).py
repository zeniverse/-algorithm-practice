s = input()
arr = ['U', 'C', 'P', 'C']
idx = 0

for a in arr:
    if a in s:
        idx += 1
        s = s[s.index(a) + 1:]
    else:
        print("I hate UCPC")
        break

if idx == 4:
    print("I love UCPC")