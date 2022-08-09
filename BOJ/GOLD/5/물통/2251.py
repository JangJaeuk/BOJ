import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

def dfs(a, b, c):
    global res
    if a == 0:
        res.append(c)
        
    if c != 0:
        if c + b >= b_size:
            if not visited[a][b_size][c-(b_size - b)]:
                visited[a][b_size][c-(b_size - b)] = True
                dfs(a, b_size, c-(b_size - b))
        else:
            if not visited[a][c+b][0]:
                visited[a][c+b][0] = True
                dfs(a, c+b, 0)
        if c + a >= a_size:
            if not visited[a_size][b][c-(a_size - a)]:
                visited[a_size][b][c-(a_size - a)] = True
                dfs(a_size, b, c-(a_size - a))
        else:
            if not visited[c+a][b][0]:
                visited[c+a][b][0] = True
                dfs(c+a, b, 0)
    if b != 0:
        if b + c >= c_size:
            if not visited[a][b-(c_size - c)][c_size]:
                visited[a][b-(c_size - c)][c_size] = True
                dfs(a, b-(c_size - c), c_size)
        else:
            if not visited[a][0][b+c]:
                visited[a][0][b+c] = True
                dfs(a, 0, b+c)
        if b + a >= a_size:
            if not visited[a_size][b-(a_size - a)][c]:
                visited[a_size][b-(a_size - a)][c] = True
                dfs(a_size, b-(a_size - a), c)
        else:
            if not visited[b+a][0][c]:
                visited[b+a][0][c] = True
                dfs(b+a, 0, c)
    if a != 0:
        if a + b >= b_size:
            if not visited[a-(b_size - b)][b_size][c]:
                visited[a-(b_size - b)][b_size][c] = True
                dfs(a-(b_size - b), b_size, c)
        else:
            if not visited[0][a+b][c]:
                visited[0][a+b][c] = True
                dfs(0, a+b, c)
        if a + c >= c_size:
            if not visited[a-(c_size - c)][b][c_size]:
                visited[a-(c_size - c)][b][c_size] = True
                dfs(a-(c_size - c), b, c_size)
        else:
            if not visited[0][b][a+c]:
                visited[0][b][a+c] = True
                dfs(0, b, a+c)

if __name__ == "__main__":
    a_size, b_size, c_size = map(int, input().split())
    visited = [[[False] * 201 for _ in range(201)] for _ in range(201)]
    res = list()

    dfs(0, 0, c_size)
    res.sort()
    res.pop()
    
    for x in res:
        print(x, end= ' ')