import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    dp = [1] * n
    
    res_list = list()
    
    for i in range(1, n):
        for j in range(i):
            if a[i] > a[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    max_dp = max(dp)
    max_index = dp.index(max_dp)    
    
    while max_dp > 0:
        res_list.append(a[max_index])
        max_dp -= 1
        while max_index >=0 and dp[max_index] != max_dp:
            max_index -= 1
    print(max(dp))
    for i in range(len(res_list)-1, -1, -1):
        print(res_list[i], end= ' ')