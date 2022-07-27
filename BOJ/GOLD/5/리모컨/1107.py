import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    target = input().rstrip()
    m = int(input())
    m_list = list(map(int, input().split()))
    min_cnt = abs(int(target) - 100)
    
    for i in range(1000001):
        num = str(i)
        for j in range(len(num)):
            if int(num[j]) in m_list:
                break
            elif j == len(num)-1:
                min_cnt = min(min_cnt, abs(int(target) - int(num)) + len(num))
    print(min_cnt)
            
    