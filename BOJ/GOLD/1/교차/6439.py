# CCW(Counter Clock Wise) 알고리즘
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

def ccw(a, b, c):
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c
    res = x1*y2 + x2*y3 + x3*y1 - (x2*y1 + x3*y2 + x1*y3)
    
    if res < 0:
        return -1
    elif res > 0:
        return 1
    else:
        return 0
def isCross(a, b, c, d):
    if (ccw(a, b, c) * ccw(a, b, d) <= 0) and (ccw(c, d, a) * ccw(c, d, b) <= 0):
        x1, y1 = a
        x2, y2 = b
        x3, y3 = c
        x4, y4 = d
        
        if (x1 < x3 and x1 < x4 and x2 < x3 and x2 < x4) or (x3 < x1 and x3 < x2 and x4 < x1 and x4 < x2):
            return False
        if (y1 < y3 and y1 < y4 and y2 < y3 and y2 < y4) or (y3 < y1 and y3 < y2 and y4 < y1 and y4 < y2):
            return False
        return True
    return False
    
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        line_x1, line_y1, line_x2, line_y2, rec_x1, rec_y1, rec_x2, rec_y2 = map(int, input().split())
        r1 = (min(rec_x1, rec_x2), min(rec_y1, rec_y2))
        r2 = (min(rec_x1, rec_x2), max(rec_y1, rec_y2))
        r3 = (max(rec_x1, rec_x2), min(rec_y1, rec_y2))
        r4 = (max(rec_x1, rec_x2), max(rec_y1, rec_y2))
        
        if (isCross((line_x1, line_y1), (line_x2, line_y2), r1, r2) or isCross((line_x1, line_y1), (line_x2, line_y2), r2, r4) or 
            isCross((line_x1, line_y1), (line_x2, line_y2), r4, r3) or isCross((line_x1, line_y1), (line_x2, line_y2), r3, r1)):
            print('T')
        else:
            if ((r1[0] < line_x1 and r1[0] < line_x2 and line_x1 < r3[0] and line_x2 < r3[0]) and 
                (r1[1] < line_y1 and r1[1] < line_y2 and line_y1 < r4[1] and line_y2 < r4[1])):
                print('T')
            else:
                print('F')