from collections import Counter
import math, copy

def dividor(str, arr):
    for i in range(len(str) - 1):
        if str[i : i + 2].isalpha():
            arr.append(str[i:i + 2])

    return arr

def getIntersection(arr1, arr2, counter1, counter2):
    interserction = list(set(arr1) & set(arr2))
    lst = []

    for i in interserction:
        repeat = min(counter1[i], counter2[i])

        for j in range(repeat):
                lst.append(i)

    return lst

def getUnion(arr1, arr2, counter1, counter2):
    union = copy.deepcopy(arr1)
    interserction = list(set(arr1) & set(arr2))
    
    for i in arr2:
        if i not in arr1:
            union.append(i)

    for i in interserction:
        repeat = max(counter1[i], counter2[i])
        actual = union.count(i)

        for j in range(abs(repeat - actual)):
                union.append(i)

    return union


def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()

    arr1 = []
    arr2 = []
    
    arr1 = dividor(str1, arr1)
    arr2 = dividor(str2, arr2)
    
    counter1 = Counter(arr1)
    counter2 = Counter(arr2)
    
    inter_length = len(getIntersection(arr1, arr2, counter1, counter2))
    union_length = len(getUnion(arr1, arr2, counter1, counter2))
    
    if inter_length == 0 and union_length == 0:
        return math.trunc(1 * 65536)
    else:
        return math.trunc((inter_length/union_length) * 65536)

print(solution('abc', 'abbb'))