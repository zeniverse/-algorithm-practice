
n = 3
lost = [1, 2]
reserve = [2, 3]

_reserve = list(set(reserve) - set(lost))
_lost = list(set(lost) - set(reserve))

_reserve.sort()
_lost.sort()

for i in _reserve:
    if i - 1 in _lost:
        _lost.remove(i - 1)
    elif i + 1 in _lost:
        _lost.remove(i + 1)

print(n - len(_lost))