s = input()

for i in s:
    if i.isalpha():
        if i.isupper():
            if ord(i) + 13 > 90:
                num = ((ord(i) + 13) % 90) - 1 + 65
            else:
                num = ord(i) + 13

            print(chr(num), end = "")
        else:
            if ord(i) + 13 > 122:
                num = ((ord(i) + 13) % 122) - 1 + 97
            else:
                num = ord(i) + 13

            print(chr(num), end = "")
    else:
        print(i, end="")
        