import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        files = [0] + list(map(int, input().split()))
        
        # 파일의 누적합
        s = [0 for _ in range(n+1)]
        for i in range(1, n+1):
            s[i] = s[i-1] + files[i]
        
        # dp[i][j] = dp[i][k] + dp[k+1][j] + (s[j] - s[i])
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
        
        # 중심 대각선과 멀어진 정도
        for dis in range(2, n+1):
            # 대각선 행
            for i in range(1, n+2-dis):
                j = i + dis - 1
                dp[i][j] = 2**32
                for k in range(i, j):
                    # 점화식
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + (s[j] - s[i-1]))
                    
        print(dp[1][n])
        
        
        
        
        
        