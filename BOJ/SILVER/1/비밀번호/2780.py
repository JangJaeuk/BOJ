import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        dp = [1] * 10
        for _ in range(1, n):
            dp0 = dp[0]
            dp1 = dp[1]
            dp2 = dp[2]
            dp3 = dp[3]
            dp4 = dp[4]
            dp5 = dp[5]
            dp6 = dp[6]
            dp7 = dp[7]
            dp8 = dp[8]
            dp9 = dp[9]
            
            dp[0] = dp7
            dp[1] = dp2 + dp4
            dp[2] = dp1 + dp5 + dp3
            dp[3] = dp2 + dp6
            dp[4] = dp1 + dp5 + dp7
            dp[5] = dp2 + dp4 + dp6 + dp8
            dp[6] = dp3 + dp5 + dp9
            dp[7] = dp4 + dp0 + dp8
            dp[8] = dp7 + dp5 + dp9
            dp[9] = dp6 + dp8
            
        print(sum(dp) % 1234567)