from collections import Counter

topping = [1, 2, 1, 3, 1, 4, 1, 2]

def solution(topping):
    res = 0
    me = Counter(topping)
    brother = set()
    me_count, bro_count = len(me), 0
    
    for i in topping:
        me[i] -= 1

        if me[i] == 0:
            me_count -= 1
        
        if i not in brother:
            brother.add(i)
            bro_count += 1

        if me_count == bro_count:
            res += 1

        if bro_count > me_count:
            break

    return res

print(solution(topping))