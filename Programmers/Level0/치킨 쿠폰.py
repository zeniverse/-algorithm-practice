
chicken = 1081

def solution(chicken):
    res = 0
    coupon = chicken

    while coupon >= 10:
        done = coupon // 10
        res += done
        coupon = coupon % 10  + done
        
    return res

print(solution(chicken))
