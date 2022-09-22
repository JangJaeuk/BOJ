import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    t = int(input())
    arr = list()
    for _ in range(t):
        cmd = list(input().split())
        n = int(cmd[0])
        string_list = cmd[1:]
        arr.append(string_list)
    arr.sort()
    print(arr)
    for i in range(len(arr[0])):
        print("--" * i + arr[0][i])
    for i in range(1, t):
        count = -1
        for j in range(len(arr[i])):
            if(len(arr[i-1]) <= j or arr[i-1][j] != arr[i][j]):
                break
            else:
                count = j
        for j in range(count + 1, len(arr[i])):
            print("--" * j + arr[i][j])