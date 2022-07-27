import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

def fibonacci(n):
    if n == 0:
        print(0)
        return 0
    elif n == 1:
        print(1)
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
    n = int(input())
    dp0 = [0] * 41
    dp1 = [0] * 41
    
    dp0[0], dp0[1] = 1, 0
    dp1[0], dp1[1] = 0, 1
    
    for i in range(2, 41):
        dp0[i] = dp0[i-1] + dp0[i-2]
        dp1[i] = dp1[i-1] + dp1[i-2]
        
    for _ in range(n):
        k = int(input())
        print(dp0[k], dp1[k])