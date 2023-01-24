import sys
from collections import deque

r,c,t = map(int,sys.stdin.readline().split())
mapp = []
air = []
dust = deque()
dirr = [-1,1,0,0]
dirc = [0,0,-1,1]

for i in range(r) : 
    # 공기청정기가 설치된 곳은 Ar,c가 -1이고, 나머지 값은 미세먼지의 양
    mapp.append(list(map(int, (sys.stdin.readline().rstrip().split()))))

# 공기청정기 찾기 => a[n][1] a[n+1][1] 의 형태로 저장될 것 
# 미세먼지 찾아서 큐에다가 넣기
for i in range(r) :
    for j in range(c) : 
        if mapp[i][j]==-1 : 
            air.append((i,j)) 
        elif mapp[i][j] > 0 :
            dust.append((i,j,mapp[i][j]))

while t : 
    # 1. 미세먼지의 확산
    now_len_dust = len(dust)
    for i in range(now_len_dust) :
        dr, dc, dq = dust.popleft()
        chk = 0 # 내 먼지를 확산시킨 방향의 갯수
        for j in range(4) :
            tmpr = dr+dirr[j] 
            tmpc = dc+dirc[j]
            # 범위 안 벗어나고 공기청정기가 아니라면 확산시키기
            if 0<=tmpr<r and 0<=tmpc<c and mapp[tmpr][tmpc]!=-1 :
                mapp[tmpr][tmpc]+= dq//5 
                chk+=1
        mapp[dr][dc]-=((dq//5) * chk)

    # 2. 공기청정기 작동

    # 2-1 : 반시계
    ar,ac = air[0]

    # 2-1-1
    q =deque(mapp[ar])
    q.appendleft(-1)
    q[1] = 0
    tmp1 = q[-1]
    q.pop()
    mapp[ar] = list(q)

    # 2-1-2 
    for i in range(ar-1,0,-1) :
        tmp2 = mapp[i][c-1]
        mapp[i][c-1] = tmp1
        tmp1 = tmp2
    
    # 2-1-3
    q =deque(mapp[0]) 
    q.append(tmp1)
    tmp1 = q.popleft()   
    mapp[0] = list(q)

    # 2-1-4
    for i in range(1, ar) :
        tmp2 = mapp[i][0]
        mapp[i][0] = tmp1
        tmp1= tmp2

    mapp[ar][ac] = -1
    
    # 2-2 : 시계
    ar,ac = air[1]

    # 2-2-1
    q = deque(mapp[ar])
    q.appendleft(-1)
    q[1] = 0
    tmp1 = q[-1]
    q.pop()
    mapp[ar] = list(q)

    # 2-2-2 
    for i in range(ar+1,r-1) :
        tmp2 = mapp[i][c-1]
        mapp[i][c-1] = tmp1
        tmp1 = tmp2

    # 2-2-3
    q =deque(mapp[r-1]) 
    q.append(tmp1)
    tmp1 = q.popleft()   
    mapp[r-1] = list(q)

    # 2-2-4
    for i in range(r-2,ar,-1) : # 처음에 이 범위 잘못 설정했었음
        tmp2 = mapp[i][0]
        mapp[i][0] = tmp1
        tmp1= tmp2

    mapp[ar][ac] = -1
    
    # 다시 미세먼지 존재 공간 검사
    for i in range(r) :
        for j in range(c) : 
            if mapp[i][j] > 0 :
                dust.append((i,j,mapp[i][j]))

    t-=1
    
# 첫째 줄에 T초가 지난 후 구사과 방에 남아있는 미세먼지의 양을 출력한다.
dust = 0
for i in range(r) :
    for j in range(c) : 
        if mapp[i][j] > 0 : 
            dust+=mapp[i][j]

print(dust)
