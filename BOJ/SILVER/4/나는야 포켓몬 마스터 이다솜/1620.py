import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    pm_dict_ns = dict()
    pm_dict_sn = dict()

    for i in range(1, n+1):
        name = input().rstrip()
        pm_dict_ns[i] = name
        pm_dict_sn[name] = i

    for _ in range(m):
        t = input().rstrip()
        if t.isdecimal():
            print(pm_dict_ns[int(t)])
        else:
            print(pm_dict_sn[t])