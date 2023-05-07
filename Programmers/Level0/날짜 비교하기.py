
def solution(date1, date2):
    d1 = date1[-1] + (date1[1] * 30) + (date1[0] * 30 * 12)
    d2 = date2[-1] + (date2[1] * 30) + (date2[0] * 30 * 12)
    return 0 if d1 >= d2 else 1

date1 = [2021, 12, 28]
date2 = [2021, 12, 29]
print(solution(date1, date2))