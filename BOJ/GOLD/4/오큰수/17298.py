import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    stack = list()
    res = [-1] * N

    for i in range(N - 1, -1, -1):
        while stack and stack[-1] <= A[i]:
            stack.pop()
        if stack:
            res[i] = stack[-1]
        stack.append(A[i])

    print(*res)
