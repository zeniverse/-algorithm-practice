
rainbow = set()
rainbow.add('ChongChong')

for _ in range(int(input())):
    a, b = input().split()

    if a in rainbow or b in rainbow:
        rainbow.add(a)
        rainbow.add(b)

print(len(rainbow))