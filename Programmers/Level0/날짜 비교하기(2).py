
def solution(date1, date2):
    return 1 if int(''.join(str(i) for i in date1)) < int(''.join(str(i) for i in date2)) else 0

date1 = [2021, 12, 28]
date2 = [2021, 12, 29]
print(solution(date1, date2))