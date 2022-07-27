import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    a = [[i] for i in range(n)]
    b = list(map(int, input().split()))
    for i in range(n):
        a[i].append(b[i])
    a.sort(key = lambda x : x[1])
    
    index = 0
    for i in range(n-1):
        a[i].append(index)
        if a[i][1] != a[i+1][1]:
            index += 1
    a[n-1].append(index)
    a.sort(key = lambda x : x[0])
    
    for i in range(n):
        print(a[i][2], end=' ')