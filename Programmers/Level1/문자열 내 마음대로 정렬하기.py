strings = ["abce", "abcd", "cdx"]
n = 2

strings.sort()
strings = sorted(strings, key=lambda x: x[n])
print(strings)