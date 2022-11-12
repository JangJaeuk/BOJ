'''
import sys
import heapq as hq
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    K, N = map(int, input().split())
    a = list(map(int, input().split()))
    heap = [x for x in a]

    cnt = 0
    res = 0

    while cnt < N:
        t = hq.heappop(heap)
        if t != res:
            res = t
            cnt += 1
            for ai in a:
                hq.heappush(heap, ai * t)

    print(res)
'''

import sys
import heapq as hq
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    K, N = map(int, input().split())
    a = list(map(int, input().split()))
    heap = [x for x in a]

    res = 0

    for _ in range(N):
        res = hq.heappop(heap)
        for ai in a:
            hq.heappush(heap, ai * res)
            if res % ai == 0:
                break
    print(res)
