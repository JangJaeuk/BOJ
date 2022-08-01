import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

def make_team(start):
    global team
    team_candidate = list()
    
    while True:
        visited[start] = True
        team_candidate.append(start)
        
        start = table[start]
        if visited[start]:
            if start in team_candidate:
                team += team_candidate[team_candidate.index(start):]
            break    

if __name__ == "__main__": 
    t = int(input())
    for _ in range(t):
        n = int(input())
        table = [0] + list(map(int, input().split()))
        visited = [False] * (n+1)
        team = list()
        
        for i in range(1, n+1):
            if not visited[i]:
                make_team(i)
        print(n - len(team))
        