
n = int(input())
dough, topping = map(int, input().split())
dough_kal = int(input())
toppings = []
res = 0

for _ in range(n):
    toppings.append(int(input()))

toppings = sorted(toppings, reverse=True)

for i in range(len(toppings) + 1):
    price = dough + (topping * i)
    res = max(res, (dough_kal + sum(toppings[:i]))//price)

print(res)
