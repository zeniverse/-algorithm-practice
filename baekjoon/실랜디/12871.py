s = input()
t = input()

str1 = ''
str2 = ''

for _ in range(len(t)):
    str1 += s

for _ in range(len(s)):
    str2 += t

if str1 == str2:
    print(1)
else:
    print(0)