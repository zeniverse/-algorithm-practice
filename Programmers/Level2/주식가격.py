prices = [1, 2, 3, 2, 3]

res = [0] * len(prices)

for i in range(len(prices)):
    for j in range(i + 1, len(prices)):
        res[i] += 1

        if prices[j] < prices[i]:
            break


print(res)
