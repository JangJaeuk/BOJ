import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

def find(v):
    if v != root_list[v]:
        root_list[v] = find(root_list[v])
    return root_list[v]

def union(v1, v2):
    v1 = find(v1)
    v2 = find(v2)
    
    if v1 < v2:
        root_list[v2] = v1
    else:
        root_list[v1] = v2
        
def is_same_set(v1, v2):
    v1 = find(v1)
    v2 = find(v2)
    
    if v1 == v2:
        return True
    else:
        return False
        
if __name__ == "__main__":
    n = int(input())
    m = int(input())
    root_list = list(range(n))
    graph = [list(map(int, input().split())) for _ in range(n)]
    path = list(map(int, input().split()))
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                union(i, j)
                
    is_possible = True
    for i in range(1, m):
        if not is_same_set(path[i-1] - 1, path[i] - 1):
            print('NO')
            break
    else:
        print('YES')
    