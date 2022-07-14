from collections import deque
import sys

r,c=map(int, sys.stdin.readline().rstrip().split())
map = [list(sys.stdin.readline().rstrip()) for _ in range(r)]
fq = deque() # 불큐
jq= deque()
rdis = [-1, 1, 0, 0]
cdis = [0, 0, -1, 1]

for rr in range(r) :
    for cc in  range(c) :
        if map[rr][cc]=='J' : 
            jrow=rr;jcol=cc;jcnt=1 # 위치와 time을 넣어주기
        elif map[rr][cc]=='F' : fq.appendleft((rr,cc, 1))  
        # 주의 : 불이 하나 이상이기 가능

# #: 벽
# .: 지나갈 수 있는 공간
# J: 지훈이의 미로에서의 초기위치 (지나갈 수 있는 공간)
# F: 불이 난 공간

while fq : # 불 먼저 체크 (불이 도달하는 시간 기록)
        fnow = fq.pop()
        for f in range(4) :
            tmprf = fnow[0]+rdis[f]
            tmpcf = fnow[1]+cdis[f]
            if 0<=tmprf<r and 0<=tmpcf<c and \
                map[tmprf][tmpcf]=="." :
                    map[tmprf][tmpcf]=str(fnow[2]+1)
                    fq.appendleft((tmprf, tmpcf, fnow[2]+1))

# ['#', '#', '#', '#']
# ['#', 'J', 'F', '#']
# ['#', 3, 2, '#']
# ['#', 4, 3, '#']

impossible = True
visited=[[0]*c for _ in range(r)]
visited[jrow][jcol]=1
jq.append((jrow, jcol, 1))

while jq:
    now=jq.pop() ; row=now[0] ; col=now[1] ; cnt=now[2]

    if row==0 or col==0 or row==r-1 or col==c-1: # 가장자리에 닿으면
        impossible=False # 가능한 것 
        print(cnt);exit() #그때 당시의 시간을 출력 & 종료

    else :
        for j in range(4) : #상하좌우
            tmprj = row+rdis[j]
            tmpcj = col+cdis[j]

            if 0<=tmprj<r and 0<=tmpcj<c and \
                visited[tmprj][tmpcj]==0 :# 범위 체크 & 방문 안했던 곳이라면

# 불이 붙을 곳인데, 현재 내 시간보다 크면 내가 가기 가능 (아직 불이 안 붙었으니)
                if map[tmprj][tmpcj].isdigit() and \
                    int(map[tmprj][tmpcj])> cnt+1: # 불인 안
                        visited[tmprj][tmpcj]=1 
                        jq.appendleft((tmprj, tmpcj, cnt+1))

# 불이 아닌 경우에도 갈 수 있지! (처음에 얘를 누락 ㅠ.ㅠ)
                elif map[tmprj][tmpcj]=="." : 
                    visited[tmprj][tmpcj]=1 
                    jq.appendleft((tmprj, tmpcj, cnt+1))

if(impossible) : print("IMPOSSIBLE") # 가장자리에 못 닿고 큐 종료됐다면 IMPOSSIBLE 출력
