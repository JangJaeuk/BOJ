import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
from bisect import bisect_left

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    lis = list()

    '''
    for i in range(n):
        if len(lis) == 0 or a[i] > lis[-1]:
            lis.append(a[i])
        else:
            lt = 0
            rt = len(lis)-1
            
            while lt <= rt:
                mid = (lt + rt) // 2
                if lis[mid] < a[i]:
                    lt = mid + 1
                else:
                    rt = mid - 1    
            lis[rt + 1] = a[i]
    '''
    for i in range(n):
        k = bisect_left(lis, a[i])
        if k >= len(lis):
            lis.append(a[i])
        else:
            lis[k] = a[i]
    print(len(lis))