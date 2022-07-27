# LCS2

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    s1 = input().rstrip()
    s2 = input().rstrip()
    lcs = ''
    s1_size, s2_size = len(s1), len(s2)
    
    dp = [[0] * (s2_size + 1) for _ in range(s1_size + 1)]
    
    for i in range(1, s1_size + 1):
        for j in range(1, s2_size + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    print(dp[-1][-1])
    
    p = dp[-1][-1]
    si = s1_size
    sj = s2_size

    while p != 0:
        if dp[si - 1][sj] == p - 1 and dp[si][sj - 1] == p - 1:
            lcs = s2[sj - 1] + lcs
            p -= 1
            si -= 1
            sj -= 1
        else:
            if dp[si - 1][sj] > dp[si][sj - 1]:
                si -= 1
            else:
                sj -= 1
    print(lcs)
                
                
            