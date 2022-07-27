import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    a = list()
    
    for _ in range(n):
        a.append(list(map(int, input().split())))

    for person in a:
        rank = 1
        for c_person in a:
            if person[0] < c_person[0] and person[1] < c_person[1]:
                rank += 1
        print(rank, end=' ')