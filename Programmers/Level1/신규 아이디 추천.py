
new_id = "...!@BaT#*..y.abcdefghijklm"

def solution(new_id):
    new_id = new_id.lower()
    answer = ''
    
    for i in new_id:
        if i.isalpha() or i.isdigit() or i in ['-', '_', '.']:
            answer += i
                
    while True:
        if '..' not in answer:
            break
        answer = answer.replace('..', '.')
    
    if answer[0] == '.':
        answer = answer[1:]
    if answer and answer[-1] == '.':
        answer = answer[:-1]

    if answer == '':
        answer = 'a'
        
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
            
            
    if len(answer) <= 2 :
        while len(answer) < 3:
            answer += answer[-1]
            
              
    return answer

print(solution(new_id))