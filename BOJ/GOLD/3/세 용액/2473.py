import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    
    min_sum = 3000000001
    
    for lp in range(n-2):
        mp = lp + 1
        rp = n - 1
        while mp < rp:
            t_sum = a[lp] + a[mp] + a[rp]
            if abs(t_sum) < min_sum:
                min_sum = abs(t_sum)
                v1, v2, v3 = a[lp], a[mp], a[rp]
            if t_sum < 0:
                mp += 1
            elif t_sum > 0:
                rp -= 1
            else:
                break
    print(v1, v2, v3)