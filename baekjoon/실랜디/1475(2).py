n = input()
dic = {i : 0 for i in range(10)}

for i in n:
    if i == '9' or i == '6':
        if dic[6] != dic[9]:
            dic[6] += 1
        else:
            dic[9] += 1
    else:
        dic[int(i)] += 1

print(max([dic[i] for i in dic]))
