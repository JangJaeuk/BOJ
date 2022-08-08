import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(start, v_list):
    global res
    if not visited[start]:
        visited[start] = True
        v_list.append(start)
        dfs(a[start], v_list)
    else:
        if start in v_list:
            res += v_list[v_list.index(start):]
        

if __name__ == "__main__":
    n = int(input())
    a = [0] * (n+1)
    res = list()
    visited = [False] * (n+1)
    for i in range(1, n+1):
        a[i] = int(input())
        
    for i in range(1, n+1):
        if not visited[i]:
            dfs(i, [])
    res.sort()
    print(len(res))
    for r in res:
        print(r)