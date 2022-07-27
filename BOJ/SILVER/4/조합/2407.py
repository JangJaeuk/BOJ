import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    
    if n == m:
        print(1)
    else:
        p = 1
        c = 1
        for i in range(m):
            p *= n
            n -= 1
        for i in range(1, m+1):
            c *= i
        print(p // c)