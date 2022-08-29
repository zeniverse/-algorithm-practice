
begin = 1
end = 10


def solution(begin, end):
    res = []
    
    for i in range(begin, end + 1):
        if i == 1:
            res.append(0)

        else:
            for j in range(2, int(i ** 0.5) + 1):
                mok = i // j

                if mok > 10 ** 7:
                    continue
                
                if i % j == 0:
                    res.append(mok)
                    break
            else:
                res.append(1)

    return res

print(solution(begin, end))
