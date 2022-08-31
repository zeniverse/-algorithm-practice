

number = "1231234"
k = 3
res = []

for num in number:
    if not res:
        res.append(num)
        continue

    if k > 0:
        while res[-1] < num:
            res.pop()
            k -= 1

            if not res or k <= 0:
                break

    res.append(num)

print(''.join(res[:len(res) - k]))





