import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    t = int(input())
    a = [0] * 11
    a[1] = 1
    a[2] = 2
    a[3] = 4
    for i in range(4, 11):
        a[i] = a[i-1] + a[i-2] + a[i-3]
    
    for i in range(t):
        tmp = int(input())
        print(a[tmp])