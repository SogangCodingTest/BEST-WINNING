from collections import deque
import sys

target = -999

def bfs(q):
    while q :
        now = q.popleft() #(0,1) 의 (x,y) 형태로 빠져나옴
        #print(now)
        for i in range(4) : #상하좌우 살펴봐야 함
            tmpr = now[0]+rloc[i] # x가 column 열이고
            tmpc = now[1]+cloc[i] # y가 row 행임 , 따라서 [tmpy][tmpx] 순서 
            if 0<=tmpr<r and \
                0<=tmpc<c and \
                    chk[tmpr][tmpc]==0 and \
                        (map[tmpr][tmpc]=='L') :
                q.append((tmpr , tmpc)) # r(행), c(열) 순으로 저장 
                chk[tmpr][tmpc] = 1
                dis[tmpr][tmpc] = dis[now[0]][now[1]]+1
                
# 행,열 값 받기
r,c = map(int,sys.stdin.readline().rstrip().split())

# 지도 받기 
map=[]
for i in range(r) :
    map.append(list(sys.stdin.readline().rstrip()))

# 상하좌우
rloc = [0,0,-1,1]
cloc = [1,-1,0,0]

land =[]

for i in range(r) :
    for j in range(c) : 
        if(map[i][j]=='L') :
            land.append((i,j)) # y가 행, x가 열 따라서 j,i 순으로 넣어줌 

for i in land : 
    start = i 

    # 초기화 작업 
    q=deque() #하나 popleft 되면 인접노드 담고,, 반복할 아이
    chk = [[0] * (c+1) for _ in range(r+1)] #방문 여부 체크
    dis = [[0] * (c+1) for _ in range(r+1)] #거리 정보 체크

    # 초기화 작업 (2) - 시작점 아이 체크 
    q.append((start[0], start[1]))
    chk[start[0]][start[1]]=1
    dis[start[0]][start[1]]=0
    #print(q)
    bfs(q)

    for i in dis :
        #print("dis " , i)
        if max(i) > target : 
            target = max(i)
print(target)

