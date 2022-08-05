sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]

print(max(max(x) for x in sizes) * max(min(x) for x in sizes))