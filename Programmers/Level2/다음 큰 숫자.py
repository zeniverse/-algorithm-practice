
n = 78

num1 = bin(n)
count1 = bin(n).count('1')

print(num1)
print(count1)

for i in range(n + 1, 1000001):
    count2 = bin(i).count('1')

    if count1 == count2:
        print(i)
        break
    


