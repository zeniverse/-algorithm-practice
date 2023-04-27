
def solution(my_string, is_suffix):
    arr = []
    for i in range(len(my_string)):
        arr.append(my_string[i:])

    return 1 if is_suffix in arr else 0

my_string = "banana"
is_suffix = "nan"
print(solution(my_string, is_suffix))