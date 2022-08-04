
n = 3

if (n**0.5).is_integer():
    target = n**0.5
    print(int(target + 1)**2)
else:
    print(-1)


print((int(n**0.5) + 1)**2 if (n**0.5).is_integer() else -1)