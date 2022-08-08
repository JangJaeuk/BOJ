import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

def move_up(t_board):    
    t_list = [[0] * n for _ in range(n)]                 
    for i in range(n):
        index = 0
        p = -1
        flag = False
        
        for j in range(n):
            if t_board[j][i] != 0:
                if not flag:
                    p = t_board[j][i]
                    flag = True
                else:
                    if p == t_board[j][i]:
                        t_list[index][i] = p * 2
                        p = -1
                        flag = False
                    else:
                        t_list[index][i] = p
                        p = t_board[j][i]
                    index += 1
        if p != -1:
            t_list[index][i] = p
                        
    return t_list
            
def move_right(t_board):    
    t_list = [[0] * n for _ in range(n)]                 
    for i in range(n):
        index = n-1
        p = -1
        flag = False
        
        for j in range(n-1, -1, -1):
            if t_board[i][j] != 0:
                if not flag:
                    p = t_board[i][j]
                    flag = True
                else:
                    if p == t_board[i][j]:
                        t_list[i][index] = p * 2
                        p = -1
                        flag = False
                    else:
                        t_list[i][index] = p
                        p = t_board[i][j]
                    index -= 1
        if p != -1:
            t_list[i][index] = p
                        
    return t_list

def move_down(t_board):                 
    t_list = [[0] * n for _ in range(n)]                 
    for i in range(n):
        index = n-1
        p = -1
        flag = False
        
        for j in range(n-1, -1, -1):
            if t_board[j][i] != 0:
                if not flag:
                    p = t_board[j][i]
                    flag = True
                else:
                    if p == t_board[j][i]:
                        t_list[index][i] = p * 2
                        p = -1
                        flag = False
                    else:
                        t_list[index][i] = p
                        p = t_board[j][i]
                    index -= 1
        if p != -1:
            t_list[index][i] = p
                        
    return t_list

def move_left(t_board):
    t_list = [[0] * n for _ in range(n)]                 
    for i in range(n):
        index = 0
        p = -1
        flag = False
        
        for j in range(n):
            if t_board[i][j] != 0:
                if not flag:
                    p = t_board[i][j]
                    flag = True
                else:
                    if p == t_board[i][j]:
                        t_list[i][index] = p * 2
                        p = -1
                        flag = False
                    else:
                        t_list[i][index] = p
                        p = t_board[i][j]
                    index += 1
        if p != -1:
            t_list[i][index] = p
                        
    return t_list

def dfs(t_board, num):
    global max_block
    if num == 5:
        for i in range(n):
            for j in range(n):
                max_block = max(max_block, t_board[i][j])
        return
    else:
        t = move_up(t_board)
        dfs(t, num + 1)
        t = move_right(t_board)
        dfs(t, num + 1)
        t = move_left(t_board)
        dfs(t, num + 1)
        t = move_down(t_board)
        dfs(t, num + 1)

if __name__ == "__main__":
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    max_block = 0
    
    dfs(board, 0)
    print(max_block)