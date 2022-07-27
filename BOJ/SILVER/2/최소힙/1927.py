import sys
import heapq as hq
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    a = list()

    for _ in range(n):
        k = int(input())
        if k == 0:
            if len(a) == 0:
                print(0)
            else:
                print(hq.heappop(a))
        else:
            hq.heappush(a, k)