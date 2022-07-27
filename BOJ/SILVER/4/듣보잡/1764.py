import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    db = dict()
    for _ in range(n):
        name = input().rstrip()
        db[name] = 1
    for _ in range(m):
        name = input().rstrip()
        if name in db:
            db[name] = 0

    dbjl = list()
    cnt = 0
    for name, v in db.items():
        if v == 0:
            cnt += 1
            dbjl.append(name)

    dbjl.sort()
    print(cnt)
    for dbj in dbjl:
        print(dbj)