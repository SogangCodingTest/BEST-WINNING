from collections import deque
import sys
# 내가 도착할 위치
n,m= map(int, sys.stdin.readline().split())
# 상하좌우
dirr = [-1,1,0,0]
dirc = [0,0,-1,1]
# 지도
mapp=[]
for _ in range(n) : 
    mapp.append(list(sys.stdin.readline().strip()))
# 방문
visit = [[[-1]*2 for _ in range(m)] for _ in range(n)]
# 큐
q=deque()
q.append((0,0,0)) # 좌표랑 벽 부숨 여부 
visit[0][0][0]=1 # 안 부숨 상태 = 0 

while q :
    
    nowr, nowc, broken = q.popleft()

    for i in range(4) : 
        if 0<=nowr+dirr[i]<n and 0<=nowc+dirc[i]<m : # 좌표만 맞는지 검사 

            # 벽이고, 부수기 가능 상태라면 
            if mapp[nowr+dirr[i]][nowc+dirc[i]] == '1' and broken==0 : 
                visit[nowr+dirr[i]][nowc+dirc[i]][1] = visit[nowr][nowc][0]+1 # 벽 부순 경우로 방문 처리 
                q.append((nowr+dirr[i], nowc+dirc[i], 1))

            # 벽 아닌 경우엔 있는 그대로 가기~ 
            elif mapp[nowr+dirr[i]][nowc+dirc[i]] == '0' and visit[nowr+dirr[i]][nowc+dirc[i]][broken]==-1:
                visit[nowr+dirr[i]][nowc+dirc[i]][broken] = visit[nowr][nowc][broken]+1
                q.append((nowr+dirr[i], nowc+dirc[i], broken))

# 만약 부수고 간거랑, 그냥 간거랑 다 유효하다면 둘 중 작은 값 
if (visit[n-1][m-1][0]!=-1 and visit[n-1][m-1][0]>0) and (visit[n-1][m-1][1]!=-1 and visit[n-1][m-1][1]>0): 
    print(min(visit[n-1][m-1][0], visit[n-1][m-1][1]))
elif (visit[n-1][m-1][0]!=-1 and visit[n-1][m-1][0]>0):
    print(visit[n-1][m-1][0])
elif (visit[n-1][m-1][1]!=-1 and visit[n-1][m-1][1]>0):
    print(visit[n-1][m-1][1])
# 어느것도 유효하지 않다면 -1 ~ 
else : 
    print(-1)
