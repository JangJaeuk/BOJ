import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    papers = [0]
    res = 0
    for _ in range(6):
        papers.append(int(input()))
    for i in range(6, 0, -1):
        # 4, 5, 6번 색종이의 경우 색종이의 개수만큼 판 필요
        if i in [4, 5, 6]:
            res += papers[i]
            if i == 5:
                # 판을 채우기 위해 필요한 1번 색종이
                need_1 = 11 * papers[i]
                papers[1] = max(papers[1] - need_1, 0)
            elif i == 4:
                # 판을 채우기 위해 필요한 2번 색종이
                need_2 = 5 * papers[i]
                if papers[2] >= need_2:
                    papers[2] -= need_2
                else:
                    papers[2] = 0
                    need_2 -= papers[2]
                # 2번으로 판을 채우고 난 뒤 필요한 1번 색종이
                need_1 = 4 * need_2
                papers[1] = max(papers[1] - need_1, 0)
        elif i == 3:
            res += (papers[i] // 4)
            rest = (papers[i] % 4)
            if rest > 0:
                res += 1
                if rest == 3:
                    papers[2] = max(papers[2] - 1, 0)
                    papers[1] = max(papers[1] - 5, 0)
                elif rest == 2:
                    papers[2] = max(papers[2] - 3, 0)
                    papers[1] = max(papers[1] - 6, 0)
                elif rest == 1:
                    papers[2] = max(papers[2] - 5, 0)
                    papers[1] = max(papers[1] - 7, 0)
        elif i == 2:
            res += (papers[i] // 9)
            rest = (papers[i] % 9)
            if rest > 0:
                res += 1
                papers[1] = max(papers[1] - (rest * 4), 0)
        elif i == 1:
            res += (papers[i] // 36)
            rest = (papers[i] % 36)
            if rest > 0:
                res += 1
    print(res)
