# 스도쿠 문제 백트래킹 연습하기 좋다

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

def getEmptyPos():
    tmp = list()
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                tmp.append((i, j))
    return tmp
def getIsPossible(x, y):
    isPossibleList = [True] * 10
    
    recX = x // 3
    recY = y // 3
    
    for i in range(3):
        for j in range(3):
            isPossibleList[board[recX*3 + i][recY*3 + j]] = False
            
    for i in range(9):
        isPossibleList[board[x][i]] = False
        
    for i in range(9):
        isPossibleList[board[i][y]] = False
        
    return isPossibleList
def dfs(index):
    if emptyPosSize <= index:
        return True
    x, y = emptyPosList[index]
    isPossibleList = getIsPossible(x, y)
    
    for i in range(1, 10):
        if isPossibleList[i]:
            board[x][y] = i
            if dfs(index + 1):
                return True
            board[x][y] = 0
    return False
    
if __name__ == "__main__":
    board = [list(map(int, input().rstrip())) for _ in range(9)]
    emptyPosList = getEmptyPos()
    emptyPosSize = len(emptyPosList)
    dfs(0)
    for i in range(9):
        for j in range(9):
            print(board[i][j], end = '')
        print()
    