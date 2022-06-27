lottos = [45, 4, 35, 20, 3, 9]
win_nums = [20, 9, 3, 45, 4, 35]
res = [0,0]

rank = '65432'

win_nums = set(list(win_nums))

same_count = 0
zero_count = 0

for i in lottos:
    if i in win_nums:
        same_count += 1
    else:
        if i == 0:
            zero_count += 1

min = rank.find(str(same_count))
max = rank.find(str(same_count + zero_count))

if max == -1:
    res[0] = 6
else:
    res[0] = max + 1

if min == -1:
    res[1] = 6
else:
    res[1] = min + 1

print(res)