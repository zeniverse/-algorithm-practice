
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

    if num == 0 and x_count == 0 : return 0
    if num == 0 and x_count  == 1 : return "x"
    if num == 0 and x_count != 0 : return str(x_count) + "x"
    if num != 0 and x_count == 0 : return str(num)
    if num != 0 and x_count == 1 : return "x + " + str(num)

    return str(x_count) + "x + " + str(num)

    

    
print(solution(polynomial))