
polynomial = "x"

def solution(polynomial):
    num = 0
    x_count = 0

    for i in polynomial.split(" + "):
        if i.isdigit():
            num += int(i)
        else:
            if len(i) == 1:
                x_count += 1
            else:
                x_count += int(i[:-1])

    res = []

    if x_count != 0:
        res.append('x' if x_count == 1 else str(x_count) + "x")
    
    if num != 0:
        res.append(str(num))

    return ' + '.join(res) if res else '0'


    
print(solution(polynomial))