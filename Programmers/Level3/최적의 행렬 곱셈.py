def solution(sizes):
    dp = [[0 for j in range(len(sizes))] for i in range(len(sizes))]
    
    for gap in range(1, len(sizes)) : 
        for s in range(0, len(sizes)-gap) : 
            e = s+gap
            
            candidate = list()
            for m in range(s, e) :
                candidate.append(
                    dp[s][m]+dp[m+1][e]+
                    sizes[s][0]*sizes[m][1]*sizes[e][1])
            dp[s][e] = min(candidate)
            
    return dp[0][-1]