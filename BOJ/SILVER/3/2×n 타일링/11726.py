import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    
    a = [0] * (n + 1)
    if n <= 2:
        print(n)
    else:
        a[1] = 1
        a[2] = 2
        
        for i in range(3, n+1):
            a[i] = a[i-1] + a[i-2]
            
        print(a[n])
        