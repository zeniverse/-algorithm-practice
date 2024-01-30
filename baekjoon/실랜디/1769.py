n = input()
count = 0

while len(n) > 1:
    n = str(sum(list(map(int, n))))
    count += 1

print(count)
if n in ["3", "6", "9"]:
    print("YES")
else:
    print("NO")

