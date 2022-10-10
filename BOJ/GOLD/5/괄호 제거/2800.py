import sys
from itertools import combinations
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    li = input().rstrip()
    stack = list()
    cd_list = list()
    res_list = set()

    for i in range(len(li)):
        if li[i] == '(':
            stack.append(i)
        elif li[i] == ')':
            si = stack.pop()
            ei = i
            cd_list.append((si, ei))

    for i in range(1, len(cd_list) + 1):
        c = combinations(cd_list, i)
        for j in c:
            t = list(li)
            for k in j:
                si, ei = k
                t[si] = ''
                t[ei] = ''
            res_list.add(''.join(t))

    res_list = list(res_list)
    res_list.sort()
    for res in res_list:
        print(res)
