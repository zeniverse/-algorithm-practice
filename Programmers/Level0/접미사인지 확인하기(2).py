
def solution(my_string, is_suffix):
    return int(my_string.endswith(is_suffix))

my_string = "banana"
is_suffix = "nan"
print(solution(my_string, is_suffix))