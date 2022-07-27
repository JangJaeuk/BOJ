import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    n, k = map(int, input().split())
    pos = [-1] * 100001
    pos[n] = 0
    
    dq = deque()
    dq.append(n)
    
    while dq:
        t = dq.popleft()
        if t == k:
            print(pos[t])
            break 
        if 0 <= t-1 < 100001 and pos[t-1]==-1:
            pos[t-1]=pos[t]+1
            dq.append(t-1)
        if 0 <= t*2 < 100001 and pos[t*2]==-1:
            pos[t*2]=pos[t]
            dq.appendleft(t*2)
        if 0 <= t+1 < 100001 and pos[t+1]==-1:
            pos[t+1]=pos[t]+1
            dq.append(t+1)