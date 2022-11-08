import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    BIT_RANGE = 1 << 10
    NUM_RANGE = 10
    MOD = 1000000000
    N = int(input())

    # dp[자리 수][맨 뒤에 올 수 있는 숫자][사용된 숫자들의 비트]
    # ex) 123 -> 0000001110
    dp = [[[0] * BIT_RANGE for _ in range(NUM_RANGE)] for _ in range(N+1)]

    # 0제외
    for i in range(1, NUM_RANGE):
        dp[1][i][1 << i] = 1

    # 자리 수
    for i in range(1, N):
        # 숫자 범위 j
        for j in range(NUM_RANGE):
            # 숫자 비트 표현
            for k in range(BIT_RANGE):
                # 맨 뒤에 있는 숫자가 0보다 크면 해당 숫자보다 1작은 숫자들이 올 수 있음
                if j > 0:
                    next = k | 1 << (j - 1)
                    dp[i+1][j-1][next] += dp[i][j][k]
                    dp[i+1][j-1][next] %= MOD
                # 맨 뒤에 있는 숫자가 9보다 작으면 해당 숫자보다 1큰 숫자들이 올 수 있음
                if j < 9:
                    next = k | 1 << (j + 1)
                    dp[i+1][j+1][next] += dp[i][j][k]
                    dp[i+1][j+1][next] %= MOD

    res = 0
    for i in range(NUM_RANGE):
        res += dp[N][i][BIT_RANGE-1]
        res %= MOD

    print(res)
