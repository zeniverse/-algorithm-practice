
res = int(input())

for _ in range(res):
    s = input()
    
    for i in range(len(s)-1):
        if s[i] != s[i + 1]:
            if s[i] in s[i + 1:]:
                res -= 1
                break

print(res)




        
