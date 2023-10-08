chemical = input()
stack = []
dic = {'H':1, 'C':12, 'O':16}

for s in chemical:
  if s =='(':
    stack.append(s)
  elif s == 'H' or s == 'C' or s == 'O':
    stack.append(dic[s])
  elif s == ')':
    temp = 0
    while True:
      if stack[-1] == '(':
        stack.pop()
        stack.append(temp)
        break
      else:
        temp+=stack.pop()
  else:
    stack.append(stack.pop()*int(s))

print(sum(stack))