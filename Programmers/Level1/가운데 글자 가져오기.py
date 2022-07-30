s = 'qwer'

size = len(s)

if size % 2 == 0:
    print(s[(size//2) - 1: (size//2) + 1])
else:
    print(s[(size//2)])
