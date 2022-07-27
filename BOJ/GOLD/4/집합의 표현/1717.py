# 집합의 표현

import sys
sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def find(v):
    if v != rootList[v]:
        rootList[v] = find(rootList[v])
    return rootList[v]
    
def union(v1, v2):
    v1 = find(v1)
    v2 = find(v2)
    
    if v1 < v2:
        rootList[v2] = v1
    else:
        rootList[v1] = v2
        
def is_same_sec(v1, v2):
    v1_root = find(v1)
    v2_root = find(v2)
    if v1_root == v2_root:
        return True
    else:
        return False
        
if __name__ == "__main__":
    n, m = map(int, input().split())
    rootList = list(range(n+1))
    
    for _ in range(m):
        op, v1, v2 = map(int, input().split())
        if op == 0:
            union(v1, v2)
        elif op == 1:
            if is_same_sec(v1, v2):
                print('YES')
            else:
                print('NO')
        