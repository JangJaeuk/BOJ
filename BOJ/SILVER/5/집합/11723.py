import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    nset = set()
    for _ in range(n):
        cmd = list(input().split())
        if cmd[0] == 'add':
            cn = int(cmd[1])
            if cn not in nset:
                nset.add(cn)
        elif cmd[0] == 'remove':
            cn = int(cmd[1])
            if cn in nset:
                nset.remove(cn)
        elif cmd[0] == 'check':
            cn = int(cmd[1])
            if cn in nset:
                print(1)
            else:
                print(0)
        elif cmd[0] == 'toggle':
            cn = int(cmd[1])
            if cn in nset:
                nset.remove(cn)
            else:
                nset.add(cn)
        elif cmd[0] == 'all':
            nset = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
        elif cmd[0] == 'empty':
            nset = set()