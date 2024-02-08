import sys

n = int(input())
arr = sys.stdin.readline().rstrip()

sum_ = 0
tmp = ''

for i in arr:
    if i.isdigit():
        tmp += i
    else:
        sum_ += int(tmp)
        tmp = ''

sum_ += int(tmp)

print(sum_ - sum(range(1, n)))