
numbers = "onefourzerosixseven"
numList = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def solution(numbers):

    for i in range(len(numList)):
        numbers = numbers.replace(numList[i], str(i))
    
    return int(numbers)


print(solution(numbers))
