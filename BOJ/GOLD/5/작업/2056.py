import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    graph = [[] for _ in range(n+1)]
    degree = [0] * (n+1)
    dp = [0] * (n+1)
    w_table = [0] * (n+1)
    for i in range(1, n+1):
        cmd = list(map(int, input().split()))
        w_table[i] = cmd[0]
        degree[i] = cmd[1]
        for e in cmd[2:]:
            graph[e].append(i)
    dq = deque()
    for i in range(1, n+1):
        if degree[i] == 0:
            dq.append(i)
            dp[i] = w_table[i]
    while dq:
        t = dq.popleft()
        for connected_V in graph[t]:
            degree[connected_V] -= 1
            dp[connected_V] = max(dp[connected_V], dp[t] + w_table[connected_V])
            if degree[connected_V] == 0:
                dq.append(connected_V)
    print(max(dp))
                
    
                
        