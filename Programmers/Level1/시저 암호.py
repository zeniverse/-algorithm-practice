# 65-90
# 97~122


s = "AaZz"
n = 25
res = ""

for i in s:
    tmp = ord(i) + n

    if i == " ":
        res += " "
    elif i.isupper():
        if tmp > 90:
            tmp -= 26
        
        res += chr(tmp%26)
    else:
        if tmp > 122:
            tmp -= 26
        
        res += chr(tmp)

print(res)


