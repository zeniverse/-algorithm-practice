lottos = [45, 4, 35, 20, 3, 9]
win_nums = [20, 9, 3, 45, 4, 35]
res = [0,0]

rank=[6,6,5,4,3,2,1]

cnt_0 = lottos.count(0)
ans = 0
for x in win_nums:
    if x in lottos:
        ans += 1

print(rank[cnt_0 + ans], rank[ans])