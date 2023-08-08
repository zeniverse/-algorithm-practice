n = int(input())
pattern = input().split("*")

for _ in range(n):
    file = input()

    if len(pattern[0]) + len(pattern[1]) > len(file):
        print("NE")
    else:
        if pattern[0] == file[:len(pattern[0])] and pattern[1] == file[-len(pattern[1]):]:
            print("DA")
        else:
            print("NE")