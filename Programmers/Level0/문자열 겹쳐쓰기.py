
def solution(my_string, overwrite_string, s):
    return my_string[:s] + overwrite_string + my_string[s+len(overwrite_string):]
     

my_string = 'aaaaaaaaa'
overwrite_string = 'bb'
s =3
print(solution(my_string, overwrite_string, s))