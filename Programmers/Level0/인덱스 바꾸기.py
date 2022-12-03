
my_string = "hello"
num1 = 1
num2 = 2

def solution(my_string, num1, num2):
    arr = list(my_string)
    arr[num1], arr[num2] = arr[num2], arr[num1]
        
    return ''.join(arr)


print(solution(my_string, num1, num2))
