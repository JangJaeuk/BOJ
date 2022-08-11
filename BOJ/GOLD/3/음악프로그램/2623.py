import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
from collections import deque

def topology():
    dq = deque()
    res = list()
    
    for i in range(1, n+1):
        if degrees[i] == 0:
            dq.append(i)
            
    while dq:
        t = dq.popleft()
        res.append(t)
        for c_v in graph[t]:
            degrees[c_v] -= 1
            if degrees[c_v] == 0:
                dq.append(c_v)
  
    if len(res) == n:
        for v in res:
            print(v)
    else:
        print(0) 

if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    degrees = [0] * (n+1)
    
    for _ in range(m):
        order_cmd = list(map(int, input().split()))
        size_order = order_cmd[0]
        order_list = order_cmd[1:]
        for i in range(1, size_order):
            s, e = order_list[i-1], order_list[i]
            graph[s].append(e)
            degrees[e] += 1
    topology()