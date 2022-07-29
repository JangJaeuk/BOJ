import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__": 
    n = int(input())
    multi = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0] * n for _ in range(n)]
    
    # 대각선
    for i in range(1, n):
        # 대각선에서 몇번째 열인지
        for j in range(0, n-i):
            # 중심 대각선과 인접한 대각선
            if i == 1:
                dp[j][j+i] = multi[j][0] * multi[j][1] * multi[j+i][1]
                continue
            dp[j][j+i] = 2**32
            for k in range(j, j+i): 
                dp[j][j+i] = min(dp[j][j+i], 
                                dp[j][k] + dp[k+1][j+i] + multi[j][0] * multi[k][1] * multi[j+i][1])
                    
        
    print(dp[0][n-1])