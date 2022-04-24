s = input()
arr = [0] * 26

for i in s:
    cnt = s.count(i)
    arr[ord(i) - ord('a')] = cnt

print(*arr)