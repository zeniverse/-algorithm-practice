for _ in range(int(input())):
    floor = int(input())
    ho = int(input())

    arr = list(range(1, ho + 1))

    for i in range(floor):
        for j in range(1, ho):
            arr[j] += arr[j - 1]

    print(arr[-1])

