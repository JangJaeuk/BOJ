import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    plist = list(map(int, input().split()))
    dp = [0] * n
    p = 0
    s, e = 0, 0
    
    for i in range(n):
        if plist[i] > p:
            p = plist[i]
            s = i
            e = i
        elif plist[i] == p:
            e = i
        
    if s > n - 1 - e:
        print('B')
    elif s < n - 1 - e:
        print('R')
    else:
        print('X')
        