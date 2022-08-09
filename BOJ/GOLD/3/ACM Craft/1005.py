import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
from collections import deque

def floyd():
    level_list = [[] for _ in range(n+1)]
    dq = deque()
    
    for i in range(1, n+1):
        if degrees[i] == 0:
            dp[i] = time[i]
            dq.append(i)
    
    while dq:
        t = dq.popleft()     
        for connected_v in graph[t]:
            degrees[connected_v] -= 1
            dp[connected_v] = max(dp[t] + time[connected_v], dp[connected_v])
            if degrees[connected_v] == 0:
                dq.append(connected_v)

    print(dp[w])


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        time = [0] + list(map(int, input().split()))
        graph = [[] for _ in range(n+1)]
        degrees = [0] * (n+1)
        dp = [0] * (n+1)
        
        for _ in range(k):
            s, e = map(int, input().split())
            degrees[e] += 1
            graph[s].append(e)
            
        w = int(input())
        
        floyd()