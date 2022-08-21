name = "JAN"

res = 0

min_move = len(name) - 1

for i, char in enumerate(name):
    res += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

    next = i + 1
    while next < len(name) and name[next] == 'A':
        next += 1

    min_move = min(min_move, i * 2 + len(name) - next, i + 2 * (len(name) - next))


res += min_move
print(res)





