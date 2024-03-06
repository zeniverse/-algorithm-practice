n = int(input())
dic = {}

for _ in range(n):
    name, log = input().split()
    if log == "enter":
        dic[name] = True
    else:
        del dic[name]

print("\n".join(sorted(dic.keys(), reverse=True)))