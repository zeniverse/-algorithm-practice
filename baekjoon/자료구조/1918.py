import sys

s = sys.stdin.readline().strip()
stack = []

for i in s:
    if i.isalpha():
        print(i, end="")
    else:
        if i == "*" or i == "/":
            while len(stack):
                if stack[-1] == "/" or stack[-1] == "*":
                    print(stack.pop(), end="")
                else:
                    break
            stack.append(i)
        elif i == "+" or i == "-":
            while len(stack):
                if stack[-1] != "(":
                    print(stack.pop(), end="")
                else:
                    break
            stack.append(i)

        elif i == "(":
            stack.append(i)
        elif i == ")":
            while stack[-1] != "(":
                print(stack.pop(), end="")
            stack.pop()

print("".join(stack[::-1]))

                

