
import re

dartResult = '1D2S#10S'

point = []
answer = []
dartResult = dartResult.replace('10', 'k')

point = ['10' if i == 'k' else i for i in dartResult]
print(point)

i = -1
sdt = ['S', 'D', 'T']

for j in point:
    if j in sdt:
        answer[i] = answer[i] ** (sdt.index(j) + 1)
    elif j == '*':
        answer[i] = answer[i] * 2

        if i != 0:
            answer[i - 1] = answer[i - 1] * 2

    elif j == '#':
        answer[i] = answer[i] * (-1)

    else:
        answer.append(int(j))
        i += 1

print(answer)
print(sum(answer))



# 정규표현식 이용한 방법

dartResult = '1D2S#10S'

p = re.compile('(\d+)([SDT])([*#]?)')
dart = p.findall(dartResult)

print(dart)


