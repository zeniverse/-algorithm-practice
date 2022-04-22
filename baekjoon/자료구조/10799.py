import sys

s = sys.stdin.readline().strip()
stack = []
res = 0

for i in range(len(s)):
    if s[i] == '(':
        stack.append("(")
    else:
        if s[i - 1] == '(':
            stack.pop()
            res += len(stack)
        else:
            stack.pop()
            res += 1

print(res)