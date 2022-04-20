n = int(input())

arr = []
num = 0

while True:
    num += 1

    if '666' in str(num):
        arr.append(num)

    if len(arr) == n:
        print(arr[n - 1])
        break