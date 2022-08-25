from collections import defaultdict

survey = ["TR", "RT", "TR"]
choices = [7, 1, 3]

indicator = ["RT", "CF", "JM", "AN"]
total = defaultdict(int)

for i in range(len(survey)):
    one, two = survey[i]
    score = choices[i] - 4

    if score < 0:
        total[one] += abs(score)
    elif score > 0:
        total[two] += abs(score)

print(total)

res = ''

res += 'T' if total['T'] > total['R'] else 'R'
res += 'F' if total['F'] > total['C'] else 'C'
res += 'M' if total['M'] > total['J'] else 'J'
res += 'N' if total['N'] > total['A'] else 'A'

print(res)

        