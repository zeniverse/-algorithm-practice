
def solution(myStr):
    myStr = myStr.replace("b", "a").replace("c", "a")
    res = [i for i in myStr.split("a") if i]
    
    return res if res else ["EMPTY"]

myStr = "baconlettucetomato"
print(solution(myStr))