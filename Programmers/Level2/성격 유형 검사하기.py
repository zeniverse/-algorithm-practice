from collections import defaultdict

survey = ["TR", "RT", "TR"]
choices = [7, 1, 3]

indicator = ["RT", "CF", "JM", "AN"]
score = [0, 3, 2, 1, 0, 1, 2, 3]

total = defaultdict(int)

for i in range(len(choices)):
    if choices[i] > 4:
        total[survey[i][1]] += score[choices[i]]
    elif choices[i] < 4:
        total[survey[i][0]] += score[choices[i]]

print(total)

res = ''

for i in indicator:
    tmp1 = total[i[0]]
    tmp2 = total[i[1]]

    if tmp1 >= tmp2:
        res += i[0]
    else:
        res += i[1]

print(res)

        