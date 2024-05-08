
n = int(input())
dic = {}

for _ in range(n):
    card = int(input())

    if card in dic:
        dic[card] += 1
    else:
        dic[card] = 1

res = sorted(dic.items(),key = lambda x : (-x[1],x[0]))
print(res[0][0])