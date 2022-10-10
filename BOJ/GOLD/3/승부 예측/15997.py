import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def dfs(cnt, score_dict, p):
    # 6경기 모두 완료 한 경우
    if cnt == 6:
        score_dict = sorted(list(score_dict.items()),
                            key=lambda k: k[1], reverse=True)

        # 1 = 2 = 3 = 4 / 4명 중 2명
        if score_dict[0][1] == score_dict[1][1] == score_dict[2][1] == score_dict[3][1]:
            answer_dict[score_dict[0][0]] += p*1/2
            answer_dict[score_dict[1][0]] += p*1/2
            answer_dict[score_dict[2][0]] += p*1/2
            answer_dict[score_dict[3][0]] += p*1/2
            return

        # 1 > 2 = 3 = 4 / 3명 중 1명
        elif score_dict[0][1] > score_dict[1][1] == score_dict[2][1] == score_dict[3][1]:
            answer_dict[score_dict[0][0]] += p
            answer_dict[score_dict[1][0]] += p*1/3
            answer_dict[score_dict[2][0]] += p*1/3
            answer_dict[score_dict[3][0]] += p*1/3
            return

        # 1 = 2 = 3 > 4 / 3명 중 2명
        elif score_dict[0][1] == score_dict[1][1] == score_dict[2][1]:
            answer_dict[score_dict[0][0]] += p*(2/3)
            answer_dict[score_dict[1][0]] += p*(2/3)
            answer_dict[score_dict[2][0]] += p*(2/3)
            answer_dict[score_dict[3][0]] += p*0.0
            return

        # 1 > 2 = 3 > 4 / 2명 중 1명
        elif score_dict[0][1] > score_dict[1][1] == score_dict[2][1]:
            answer_dict[score_dict[0][0]] += p
            answer_dict[score_dict[1][0]] += p*0.5
            answer_dict[score_dict[2][0]] += p*0.5
            answer_dict[score_dict[3][0]] += p*0.0
            return

        # 그 외
        else:
            answer_dict[score_dict[0][0]] += p
            answer_dict[score_dict[1][0]] += p
            answer_dict[score_dict[2][0]] += p*0.0
            answer_dict[score_dict[3][0]] += p*0.0
            return

    # A 승
    score_dict[match_list[cnt][0]] += 3
    dfs(cnt+1, score_dict, p*float(match_list[cnt][2]))
    score_dict[match_list[cnt][0]] -= 3

    # 비김
    score_dict[match_list[cnt][0]] += 1
    score_dict[match_list[cnt][1]] += 1
    dfs(cnt+1, score_dict, p*float(match_list[cnt][3]))
    score_dict[match_list[cnt][0]] -= 1
    score_dict[match_list[cnt][1]] -= 1

    # A 패
    score_dict[match_list[cnt][1]] += 3
    dfs(cnt+1, score_dict, p*float(match_list[cnt][4]))
    score_dict[match_list[cnt][1]] -= 3


if __name__ == "__main__":
    nation1, nation2, nation3, nation4 = map(str, input().split())
    match_list = [list(input().split()) for _ in range(6)]

    score_dict = {nation1: 0, nation2: 0, nation3: 0, nation4: 0}
    answer_dict = {nation1: 0.0, nation2: 0.0, nation3: 0.0,
                   nation4: 0.0}

    dfs(0, score_dict, 1)

    for key in score_dict:
        print(answer_dict[key])
