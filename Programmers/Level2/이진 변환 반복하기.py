
s = "1111111"

res = [0, 0]

while True:

    if s == '1':
        print(res)
        break

    num = ''.join([i for i in s if i == '1'])
    
    res[0] += 1
    res[1] += len(s) - len(num)

    num = len(num)
    s = bin(int(num))[2:]


