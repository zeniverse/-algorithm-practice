my_string = "nice to meet you"

vowel = ['a', 'e', 'i', 'o', 'u']
def solution(my_string):

    for i in vowel:
        my_string = my_string.replace(i, '')
    return my_string

print(solution(my_string))
