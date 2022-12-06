
id_pw = ["programmer01", "15789"]
db = [["programmer02", "111111"], ["programmer00", "134"], ["programmer01", "1145"]]

def solution(id_pw, db):
    
    for id, password in db:
        if id == id_pw[0]:
            if password == id_pw[1]:
                return "login"
            else:
                return "wrong pw"
    return "fail"

print(solution(id_pw, db))
