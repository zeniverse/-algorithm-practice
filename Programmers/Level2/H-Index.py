citations = [3, 0, 6, 1, 5]
citations.sort()

length = len(citations)
res = 0

for i in range(length):
    if citations[i] >= length - i: # h번 이상 인용된 논문이 h편 이상
        res = length - i
        break

print(res)

