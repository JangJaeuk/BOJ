import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

def rotation_wheel(wheel, dir):
    if dir == 1:
        return wheel[7] + wheel[:7]
    elif dir == -1:
        return wheel[1:] + wheel[0]

if __name__ == "__main__":
    wheels = [input().rstrip() for _ in range(4)]
    k = int(input())
    for _ in range(k):
        w_index, rot_dir = map(int, input().split())
        w_index = w_index - 1

        lp = w_index
        rp = w_index

        i_list = list()
        i_list.append((w_index, rot_dir))

        while lp > 0 or rp < 3:
            rot_dir = -rot_dir
            is_break = True
            if lp > 0 and wheels[lp][6] != wheels[lp-1][2]:
                lp -= 1
                i_list.append((lp, rot_dir))
                is_break = False
            if rp < 3 and wheels[rp][2] != wheels[rp+1][6]:
                rp += 1
                i_list.append((rp, rot_dir))
                is_break = False
            if is_break:
                break

        for wi, d in i_list:
            wheels[wi] = rotation_wheel(wheels[wi], d)

    score = 0

    for i, wheel in enumerate(wheels):
        # s극
        if wheel[0] == '1':
            if i == 0:
                score += 1
            elif i == 1:
                score += 2
            elif i == 2:
                score += 4
            elif i == 3:
                score += 8
    print(score)