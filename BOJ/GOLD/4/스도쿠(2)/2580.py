# 스도쿠

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

def getEmptyPos():
    emptyList = list()
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                emptyList.append((i, j))
    return emptyList

def possibleNums(x, y):
    recX = x // 3
    recY = y // 3
    isPossibleList = [True] * 10
    
    for i in range(3):
        for j in range(3):
            if board[recX * 3 + i][recY * 3 + j] != 0:
                isPossibleList[board[recX * 3 + i][recY * 3 + j]] = False
                
    for i in range(9):
        if board[x][i] != 0:
            isPossibleList[board[x][i]] = False
            
    for j in range(9):
        if board[j][y] != 0:
            isPossibleList[board[j][y]] = False
            
    return isPossibleList

def dfs(index):
    if index >= emptyListSize:
        return True
    else:
        x, y = emptyList[index][0], emptyList[index][1]
        isPossibleList = possibleNums(x, y)
        for i in range(1, 10):
            if isPossibleList[i]:
                board[x][y] = i
                if dfs(index + 1):
                    return True
                board[x][y] = 0
        return False
            
if __name__ == "__main__":
    board = [list(map(int, input().split())) for _ in range(9)]
    emptyList = getEmptyPos()
    emptyListSize = len(emptyList)
    dfs(0)
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=' ')
        print()