from collections import Counter

topping = [1, 2, 1, 3, 1, 4, 1, 2]

def solution(topping):
    res = 0
    me = Counter(topping)
    bro = set()

    for i in topping:
        me[i] -= 1
        bro.add(i)

        if me[i] == 0:
            me.pop(i)
        
        if len(me) == len(bro):
            res += 1

    return res

print(solution(topping))