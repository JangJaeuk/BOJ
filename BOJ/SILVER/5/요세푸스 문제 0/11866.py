import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    n, k = map(int, input().split())
    dq = deque(list(range(1, n+1)))
    cnt = 0
    print('<', end = '')
    while len(dq) > 1:
        cnt += 1
        if cnt < k:
            dq.append(dq.popleft())
        else:
            print(dq.popleft(), end = ', ')
            cnt = 0
    print(str(dq.popleft())+'>')