import sys
sys.setrecursionlimit(10**6)
row, col = map(int, sys.stdin.readline().rstrip().split())
rdis = [-1,1,0,0] ; cdis = [0,0,-1,1]
map = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(row)]

def dfs(time, r,c) :
    for i in range(4) :
        tmpr= r+rdis[i]
        tmpc = c+cdis[i]

        if 0<=tmpr<row and 0<=tmpc<col and\
            map[tmpr][tmpc]==1 and visited[tmpr][tmpc]==0:
            map[tmpr][tmpc]=-time # 녹을 치즈 발견 시 -time 으로 갱신 
            visited[tmpr][tmpc] = 1 # 방문 표시 

        elif 0<=tmpr<row and 0<=tmpc<col and\
            map[tmpr][tmpc]==0 and visited[tmpr][tmpc]==0:
            visited[tmpr][tmpc] = 1 # 공기 발견하면 계속 탐색 진행 
            dfs(time, tmpr, tmpc) 

for k in map :
    if 1 in k : begin = True
time = 0

while begin : 

    time+=1 # 시간 일초 씩 갱신 
    visited = [[0]*col for _ in range(row)] # 방문 매번 새롭게 갱신 
    visited[0][0] = 1
    dfs(time,0,0)

    lastcheese = 0

    for m in range(row) :
        for mm in range(col) :
            if map[m][mm] == -time : # -time으로 변했던 녹을 치즈들을 0으로 바꿔주며
                map[m][mm]  = 0
                lastcheese+=1 # 녹은 치즈 갯수세기 
    begin = False

    for k in map : # 치즈가 남아있다면 one more time 
        if 1 in k : begin = True; break

print(time)
print(lastcheese)
