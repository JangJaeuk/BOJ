# 각 노드의 부모 노드 출력하기 접근 자체를 잘못

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(parent_node):
    for node in tree[parent_node]:
        if parents[node] == 0:
            parents[node] = parent_node
            dfs(node)
    
if __name__ == "__main__":
    n = int(input())
    tree = [[] for _ in range(n+1)]
    parents = [0] * (n+1)
    for _ in range(n-1):
        node1, node2 = map(int, input().split())
        tree[node1].append(node2)
        tree[node2].append(node1)
    parents[1] = -1
    
    dfs(1)
    
    for i in range(2, n+1):
        print(parents[i])