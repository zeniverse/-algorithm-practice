a = int(input())
b = int(input())

arr_b = [int(i) for i in str(b)]
arr_b.reverse()

for i in arr_b:
    print(a * i)

print(a * b)