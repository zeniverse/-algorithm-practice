s = input()
res = 0

for i in range(52):
    for j in range(i + 1, 52):
        if s[i] == s[j]:
            tmp = s[i:j + 1]

            for k in tmp:
                if tmp.count(k) == 1:
                    res += 1
            break

print(res//2)