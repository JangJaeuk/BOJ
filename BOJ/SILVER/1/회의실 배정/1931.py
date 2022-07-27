import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    schedule_table = list()
    for _ in range(n):
        schedule_table.append(list(map(int, input().split())))
    schedule_table.sort(key = lambda x: (x[1], x[0]))
    end_time = schedule_table[0][1]
    index = 1
    cnt = 1
    while index < n:
        for i in range(index, n):
            if schedule_table[i][0] >= end_time:
                index = i+1
                cnt += 1
                end_time = schedule_table[i][1]
                break
        else:
            break
    print(cnt)