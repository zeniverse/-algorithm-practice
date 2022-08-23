
from collections import Counter
import math, copy


str1 = 'abc'
str2 = 'abbb'

str1 = str1.upper()
str2 = str2.upper()

arr1 = []
arr2 = []

def dividor(str, arr):
    for i in range(len(str) - 1):
        if str[i : i + 2].isalpha():
            arr.append(str[i:i + 2])

    return arr

arr1 = dividor(str1, arr1)
arr2 = dividor(str2, arr2)

def getIntersection(arr1, arr2):
    interserction = list(set(arr1) & set(arr2))

    lst = []

    counter1 = Counter(arr1)
    counter2 = Counter(arr2)

    for i in interserction:
        repeat = min(counter1[i], counter2[i])

        for j in range(repeat):
                lst.append(i)

    return lst

intersection_length = len(getIntersection(arr1, arr2))

def getUnion(arr1, arr2):
    union = copy.deepcopy(arr1)
    interserction = list(set(arr1) & set(arr2))

    counter1 = Counter(arr1)
    counter2 = Counter(arr2)

    for i in interserction:
        repeat = max(counter1[i], counter2[i])

        for j in range(repeat - 1):
                union.append(i)

    return union

union_length = len(getUnion(arr1, arr2))

if intersection_length == 0 and union_length == 0:
    res = math.trunc(1 * 65536)
else:
    res = math.trunc((intersection_length/union_length) * 65536)
print(res)

