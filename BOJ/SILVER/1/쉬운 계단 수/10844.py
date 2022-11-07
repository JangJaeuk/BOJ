import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    dp = [[0] * 10 for _ in range(N+1)]
    # 1 ~ 9까지. 0은 맨 앞에 올 수 없음
    for i in range(1, 10):
        dp[1][i] = 1

    # dp[자리수][뒤에 올 수 있는 숫자]
    # 자리수 i
    for i in range(2, N+1):
        # 숫자 범위 j
        for j in range(10):
            # 맨 뒤에 있는 숫자가 0이면 뒤에 올 수 있는 숫자는 1만 가능
            if j == 0:
                dp[i][j] = dp[i-1][1]
            # 맨 뒤에 있는 숫자가 9이면 뒤에 올 수 있는 숫자는 8만 가능
            elif j == 9:
                dp[i][j] = dp[i-1][8]
            # 그 외에는 맨 뒤에 있는 숫자 +- 1
            else:
                dp[i][j] = dp[i-1][j+1] + dp[i-1][j-1]
    print(sum(dp[N]) % 1000000000)
