import sys
from collections import defaultdict
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))

    before_sort = defaultdict(int)
    for i in range(n):
        before_sort[a[i]] = i

    a.sort()

    after_sort = defaultdict(int)
    for i in range(n):
        after_sort[a[i]] = i

    res = 0
    for num in before_sort:
        dis = before_sort[num] - after_sort[num]
        if dis > 0 and dis > res:
            res = dis

    print(res)
