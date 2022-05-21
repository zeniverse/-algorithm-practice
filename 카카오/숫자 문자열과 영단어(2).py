s = "23four5six7"
arr = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
res = ""
tmp = ""

for i in s:
    if i.isdigit():
        if tmp:
            res += str(arr.index(tmp))
            tmp = ""
        res += i
    else:
        if tmp in arr:
            res += str(arr.index(tmp))
            tmp = i
        else:
            tmp += i
if tmp:
    res += str(arr.index(tmp))
print(res)
