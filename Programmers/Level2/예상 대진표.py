

n = 8
a = 2
b = 3



def solution(n, a, b):
    arr = [i for i in range(1, n + 1)]
    count = 0

    while True:
        
        tmp = []
        for i in range(0, len(arr), 2):
            tmp.append((arr[i], arr[i + 1]))
        
        print('tmp : ',tmp)
        count += 1
        n //= 2

        for index in range(len(tmp)):
            if a in tmp[index]:
                if b in tmp[index]:
                    return count
                else:
                    arr[index] = a

            elif b in tmp[index]:
                arr[index] = b

            else:
                arr[index] = tmp[index][0]

        arr = arr[:n]
        print(arr)


print(solution(n, a, b))

