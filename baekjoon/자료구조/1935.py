import sys

n = int(sys.stdin.readline().strip())
s = sys.stdin.readline().strip()
num_list = [int(sys.stdin.readline().strip()) for _ in range(n)]

stack = []


for i in s:
    if i.isalpha():
        num = ord(i) - ord('A')
        stack.append(num_list[num])
    else:
        b = stack.pop()
        a = stack.pop()
        
        if i == "*":
            c = a * b
        elif i == '+':
            c = a + b
        elif i == "-":
            c = a - b
        else:
            c = a/ b

        stack.append(c)
print("{:0.2f}".format(stack.pop()))