import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    n, k = map(int, input().split())
    table = [False for _ in range(n+1)]
    res = -1
    for i in range(2, n+1):
        if k == 0:
            break
        if not table[i]:
            for j in range(i, n+1, i):
                if not table[j]:
                    table[j] = True
                    k -= 1
                    if k == 0:
                        res = j
                        break
        
    print(res)
                    
    