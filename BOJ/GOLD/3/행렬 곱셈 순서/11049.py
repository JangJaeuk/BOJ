import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__": 
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0] * n for _ in range(n)]
    
    # 중심 대각선과 멀어진 정도
    for dis in range(1, n):
        # 대각선
        for i in range(n-dis):
            j = i+dis
            # 멀어진 정도가 1이면
            if dis == 1:
                dp[i][j] = matrix[i][0] * matrix[j][0] * matrix[j][1]
                continue
            dp[i][j] = 2 ** 32
            for k in range(i, j):
                # 점화식
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + matrix[i][0] * matrix[k][1] * matrix[j][1])
    print(dp[0][n-1])