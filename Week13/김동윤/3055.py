from collections import deque
import sys

r,c = map(int, sys.stdin.readline().rstrip().split())
mapp = []
for rr in range(r) :
    mapp.append(list(sys.stdin.readline().rstrip()))

water_map = list([-1 for _ in range(c)] for _ in range(r))
# 물이 차오르는 시간 저장 (-1 아니면 방문했다는 것이므로 방문 처리도 곁들임 )

godo_map = list([-1 for _ in range(c)] for _ in range(r))
# 고슴도치 시간 기록 (-1 아니면 방문했다는 것이므로 방문 처리도 곁들임 )

# 고슴도치는 현재 있는 칸과 인접한 네 칸 중 하나로 이동,  물이 있는 칸과 
# 인접해있는 비어있는 칸(적어도 한 변을 공유)은 물이 차
# 상하좌우 살펴주고 비버의 소굴(D)로 이동할 수 없

rdir = [-1, 1, 0, 0]
cdir = [0, 0, -1, 1]

# 비어있는 곳은 '.'로 표시되어 있고, 
# 물이 차있는 지역은 '*', 
# 돌은 'X'로 표시되어 있다. 
# 비버의 굴은 'D'로, 
# 고슴도치의 위치는 'S'로

water=deque() # 물 위치 담을 
for row in range(r) :
    for col in range(c) : 

        if mapp[row][col] == 'S' : # 시작위치 godo
            godo = (row,col)
            mapp[row][col] = "." # 물이 갈 수 있게 . 으로 바꿔줌 
            godo_map[row][col] = 0 # 방문처리, 시간 0초 시작 

        
        elif mapp[row][col] == '*' : # 물 큐에 저장 
            water.append((row,col))
            water_map[row][col] = 0 # 원래부터 물이면 0초 시작 ! 

        elif mapp[row][col] == 'D' :
            destination = (row,col)
            
# water 차오르는 시간 기록 
while water : 
    noww= water.popleft()
    wr,wc = noww[0], noww[1]
    for i in range(4) :
        if 0<=wr+rdir[i]<r and 0<=wc+cdir[i]<c \
                        and mapp[wr+rdir[i]][wc+cdir[i]] == '.' \
                            and water_map[wr+rdir[i]][wc+cdir[i]] ==-1 :
    
            water_map[wr+rdir[i]][wc+cdir[i]] = water_map[wr][wc] +1
            water.append((wr+rdir[i],wc+cdir[i] ))

# 고슴도치가 갈 수 있는 곳을 waterMap과 비교해 waterMap보다 작으면 갈 수 있게 
# 단, 동시에 물과 고슴도치가 도착하는 경우도 이동할 수 없으므로 +1로 비교 
q=deque()
q.append(godo)
while q:
    x, y = q.popleft()
    for i in range(4):
        dx = x + rdir[i] 
        dy = y + cdir[i] 
        # 범위, 이동가능, 방문 여부, (물 시간이 내 다음 시간보다 느리거나(크거나) or 물이 방문하지 않은 곳) 체크 
        if 0 <= dx < r and 0 <= dy < c and \
            mapp[dx][dy] in ['.', 'D'] and \
                godo_map[dx][dy] == -1 and\
                (godo_map[x][y] + 1 < water_map[dx][dy] or water_map[dx][dy] == -1):
                # 다음 시간에 물이 찰 곳인지 여부 검사 
                godo_map[dx][dy] = godo_map[x][y] + 1
                q.append([dx, dy])

if godo_map[destination[0]][destination[1]]==-1 : 
    print('KAKTUS')
else:
    print(godo_map[destination[0]][destination[1]])    
