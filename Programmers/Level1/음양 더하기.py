absolutes = [4,7,12]
signs = [True,False,True]
res = 0

for i in range(len(absolutes)):
    if signs[i]:
        res += absolutes[i]
    else:
        res -= absolutes[i]

print(res)

