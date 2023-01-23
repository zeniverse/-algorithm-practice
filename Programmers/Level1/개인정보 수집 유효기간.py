from datetime import datetime
# from dateutil.relativedelta import relativedelta

def solution(today, terms, privacies):
    res = []
    
    today = today.replace(".", "")
    today = datetime.strptime(today, '%Y%m%d')
    
    for i in range(len(privacies)):
        d, s= privacies[i].split(" ")
        d = d.replace(".", "")
        t = 0
        
        for term in terms:
            term = term.split(" ")
            if term[0] == s:
                t = int(term[1])
                
        # lastDate = datetime.strptime(d, '%Y%m%d') + relativedelta(months=t)
        
        # if lastDate <= today:
        #     res.append(i + 1)
    
    return res