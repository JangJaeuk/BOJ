import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    res = 0
    graph = list()
    for _ in range(n):
        graph.append(int(input()))
    graph.append(0)

    stack = list()
    stack.append((0, graph[0]))
    left = 0

    for i in range(1, n+1):
        left = i
        while stack and stack[-1][1] > graph[i]:
            left, h = stack.pop()
            res = max(res, (i-left) * h)
        stack.append((left, graph[i]))

    print(res)
