import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    k = int(input())

    for _ in range(k):
        n, m = map(int, input().split())
        a = list(map(int, input().split()))
        dq = [[] for _ in range(n)]

        for h in range(n):
            dq[h] = [a[h], h]
        dq = deque(dq)
        
        cnt = 0

        while dq:
            t = dq.popleft()
            if any (tt[0] > t[0] for tt in dq):
                dq.append(t)
            else:
                cnt += 1
                if t[1] == m:
                    print(cnt)
                    break