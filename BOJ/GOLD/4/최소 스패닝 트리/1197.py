import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

def find(v):
    if v != root[v]:
        root[v] = find(root[v])
    return root[v]

def union(v1, v2):
    v1 = find(v1)
    v2 = find(v2)
    
    if v1 < v2:
        root[v2] = v1
    else:
        root[v1] = v2
        
def is_connected(v1, v2):
    v1 = find(v1)
    v2 = find(v2)
    
    if v1 == v2:
        return True
    else:
        return False

def kruskal():
    sum_w = 0
    edge_info.sort(key = lambda x: x[2])
    for v1, v2, weight in edge_info:
        if not is_connected(v1, v2):
            sum_w += weight
            union(v1, v2)
    return sum_w

if __name__ == "__main__":
    v, e = map(int, input().split())
    edge_info = list()
    root = list(range(v+1))
    for _ in range(e):
        edge_info.append(list(map(int, input().split())))
    print(kruskal())