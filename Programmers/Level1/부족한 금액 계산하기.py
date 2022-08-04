price = 3
money = 20
count = 4

total = sum(i * price for i in range(1, count + 1))
res = money - total

print(abs(res) if res < 0 else 0)










