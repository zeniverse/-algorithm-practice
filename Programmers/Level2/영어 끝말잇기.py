n = 5
words = ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]

res = [0, 0]

words = [(idx, word) for idx, word in enumerate(words, start = 1)]
print(words)

s = set()
s.add(words[0][1])
check = ''

for i in range(1, len(words)):
    if words[i][1][0] != words[i - 1][1][-1]:
        check = words[i]
        break

    if words[i][1] not in s:
        s.add(words[i][1])
    else:
        check = words[i]
        break

print(s)

if check:
    print(check)
    if check[0] % n:
        res[0] = check[0] % n
        res[1] = (check[0] // n) + 1
    else:
        res[0] = n
        res[1] = check[0] // n


print(res)