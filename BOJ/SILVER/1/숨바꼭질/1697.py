import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
	n, k = map(int, input().split())
	pos = [-1] * 100001
	pos[n] = 0
	dq = deque()
	dq.append(n)

	while dq:
		t = dq.popleft()
		if t == k:
			print(pos[t])
			break
		for tp in [t+1, t-1, 2*t]:
			if 0 <= tp < 100001 and pos[tp] == -1:
				pos[tp] = pos[t] + 1
				dq.append(tp)