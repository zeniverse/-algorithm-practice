import math

str1 = 'abc'
str2 = 'abbb'

arr1 = [str1[i:i + 2].upper() for i in range(len(str1) - 1) if str1[i:i + 2].upper().isalpha()]
arr2 = [str2[i:i + 2].upper() for i in range(len(str2) - 1) if str2[i:i + 2].upper().isalpha()]

print(arr1)
print(arr2)

inter = sum([min(arr1.count(u), arr2.count(u)) for u in list(set(arr1) & set(arr2))])
union = sum([max(arr1.count(n), arr2.count(n)) for n in list(set(arr1) | set(arr2))])

if inter == 0 and union == 0:
    print(65536)
else:
    print(math.trunc((inter/union) * 65536))