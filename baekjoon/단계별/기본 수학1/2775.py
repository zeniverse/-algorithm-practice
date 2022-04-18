for _ in range(int(input())):
    floor = int(input())
    ho = int(input())

    arr = [[0] * (ho + 1) for _ in range(floor + 1)]

    for i in range(ho + 1):
        arr[0][i] = i
    
    for i in range(1, floor + 1):
        for j in range(1, ho  + 1):
            for k in range(1, j + 1):
                arr[i][j] += arr[i - 1][k]
    
    print(arr[floor][ho])