import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    x = list()
    y = list()
    
    s = 0
    
    for _ in range(n):
        tx, ty = map(int, input().split())
        x.append(tx)
        y.append(ty)
        
    x.append(x[0])
    y.append(y[0])
    
    for i in range(n):
        s += x[i]*y[i+1] - x[i+1]*y[i]
    
    print(round(abs(s/2), 1))                                                                                                                      