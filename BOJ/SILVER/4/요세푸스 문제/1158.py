import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    n, k = map(int, input().split())
    dq = deque(list(range(1, n+1)))
    res = list()
    cnt = 0

    while dq:
        t = dq.popleft()
        cnt += 1
        if cnt == k:
            res.append(t)
            cnt = 0
        else:
            dq.append(t)

    print('<', end='')
    for i in range(n):
        if i == n - 1:
            print(res[i], end='')
        else:
            print(str(res[i])+', ', end='')
    print('>')
