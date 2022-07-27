# 용액

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    lp = 0
    rp = len(a) - 1
    min_d = 2147000000
    lv = 0
    rv = 0
    
    while lp < rp:
        if abs(a[rp] + a[lp]) < min_d:
            min_d = abs(a[rp] + a[lp])
            lv = a[lp]
            rv = a[rp]
        if a[rp] + a[lp] > 0:
            rp -= 1
        else:
            lp += 1
            
    print(lv, rv)
        