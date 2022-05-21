s = "23four5six7"
num_dict = {"zero" : '0', "one" : '1', "two" : '2', "three" : '3', "four" : '4', "five" : '5', "six" : '6', "seven" : '7', "eight" : '8', "nine" : '9'}
res = ""
tmp = ""

for i in s:
    if i.isdigit():
        if tmp:
            res += num_dict[tmp]
            tmp = ""
        res += i
    else:
        if tmp in num_dict:
            res += num_dict[tmp]
            tmp = i
        else:
            tmp += i
if tmp:
    res += num_dict[tmp]
print(res)
