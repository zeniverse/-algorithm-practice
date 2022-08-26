s = "-1 -2 -3 -4"
s = list(map(int,s.split(" ")))
s.sort()

print(str(s[0]), str(s[-1]))
        