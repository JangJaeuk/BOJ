import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    lis = [0]

    for i in range(n):
        if a[i] > lis[-1]:
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
    print(len(lis) - 1)