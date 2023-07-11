import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    sounds = list(input().split())

    while True:
        animal = list(input().split())

        if animal[0] == "what":
            print(" ".join(sounds))
            break

        while animal[2] in sounds:
            sounds.remove(animal[2])
