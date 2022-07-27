import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
from collections import deque

if __name__ == "__main__":
    n = int(input())
    a = [0] * (n+1)
    s_list = deque()
    answer = 0
    sum_n = 0

    for i in range(2, n+1):
        if a[i] == 0:
            s_list.append(i)
            sum_n += i
            while sum_n > n:
                sum_n -= s_list.popleft()
            if sum_n == n:
                answer += 1
                sum_n -= s_list.popleft()
            for j in range(i, n+1, i):
                a[j] = 1
    print(answer)