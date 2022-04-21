for _ in range(int(input())):
    arr = list(input().split())

    for word in arr:
        print(word[::-1], end=" ")
    
    print()