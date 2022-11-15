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
            print(cnt + 1, '번째 숫자', str(t)+',', end=' ')
            res = t
            cnt += 1
            for ai in a:
                hq.heappush(heap, ai * t)
            print(heap)
        else:
            print(heap)

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

    for i in range(N):
        res = hq.heappop(heap)
        print(i + 1, '번째 숫자', str(res)+',', end=' ')
        for ai in a:
            hq.heappush(heap, ai * res)
            if res % ai == 0:
                break
        print(heap)
    print()
    print(res)
