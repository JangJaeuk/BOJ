import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

# + 방향
dx = [0, -1, 0, 1, 0]
dy = [0, 0, 1, 0, -1]

# 스위치 누름
def push(xx, yy, board):
    for h in range(5):
        x = xx + dx[h]
        y = yy + dy[h]
        if 0 <= x < 10 and 0 <= y < 10:
            if board[x][y] == '#':
                board[x][y] = 'O'
            elif board[x][y] == 'O':
                board[x][y] = '#'
         
# 마지막 행의 전구가 모두 꺼져있는지 확인       
def is_off(board):
    for i in range(10):
        if board[9][i] == 'O':
            return False
    return True
 
if __name__ == "__main__":
    a = [list(input().rstrip()) for _ in range(10)]
    res = 101
    
    # 비트마스킹 2^10의 경우의 수
    for bit in range(1 << 10):
        tmp = [a[i][:] for i in range(10)]
        cnt = 0
        for i in range(10):
            if bit & (1 << i):
                cnt += 1
                push(0, i, tmp)
                
        # 나머지 행은 위의 행이 켜져있으면 스위치를 누름
        for i in range(1, 10):
            for j in range(10):
                if tmp[i-1][j] == 'O':
                    cnt += 1
                    push(i, j, tmp)
                    
        # 위 작업을 계속한 후 마지막 열이 다 꺼져있으면 모두 끄는데 성공
        if is_off(tmp):
            res = min(res, cnt)
            
    if res == 101:
        print(-1)
    else:
        print(res)
        
        
            
        