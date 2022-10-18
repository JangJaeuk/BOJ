import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    s1 = input().rstrip()
    s2 = input().rstrip()
    s3 = input().rstrip()

    s1_size, s2_size, s3_size = len(s1), len(s2), len(s3)

    dp = [[[0] * (s3_size + 1) for _ in range(s2_size + 1)]
          for _ in range(s1_size + 1)]

    for i in range(1, s1_size + 1):
        for j in range(1, s2_size + 1):
            for k in range(1, s3_size + 1):
                if s1[i - 1] == s2[j - 1] == s3[k - 1]:
                    dp[i][j][k] = max(dp[i][j][k], dp[i-1][j-1][k-1] + 1)
                else:
                    dp[i][j][k] = max(dp[i-1][j][k],
                                      dp[i][j-1][k], dp[i][j][k-1])

    print(dp[-1][-1][-1])
