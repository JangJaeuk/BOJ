import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

def div(s, r, c):
    global cnt0, cnt1
    
    is_white = True
    is_blue = True
    
    for i in range(r, r + s):
        for j in range(c, c + s):
            if a[i][j] == 1:
                is_white = False
                break
        if not is_white:
            break
    
    for i in range(r, r + s):
        for j in range(c, c + s):
            if a[i][j] == 0:
                is_blue = False
                break
        if not is_blue:
            break
    
    if is_white:
        cnt0 += 1
        return
    elif is_blue:
        cnt1 += 1
        return
    else:
        s = s // 2
        div(s, r, c)
        div(s, r+s, c)
        div(s, r, c+s)
        div(s, r+s, c+s)
        
if __name__ == "__main__":
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    
    cnt0 = 0
    cnt1 = 0
    
    div(n, 0, 0)
    
    print(cnt0)
    print(cnt1)
                    