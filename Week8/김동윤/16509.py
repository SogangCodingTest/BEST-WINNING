from collections import deque
import sys
mapp = [[0 for _ in range(9)] for _ in range(10)]

# 상의 위치
r1, c1 = map(int,sys.stdin.readline().strip().split())
# 왕의 위치
r2, c2 = map(int,sys.stdin.readline().strip().split())

# 상이 왕에게 도달할 수 있는 최소 이동 횟수를 출력
# 만약 도달할 수 없다면 -1을 출력

#상 하 좌 우
x=[-1,1,0,0]
y=[0,0,-1,1]
xx=[-2,-2,2,2,1,-1,-1,1]
yy=[2,2,-2,2,-2,-2,2,2]
q = deque()
cnt = 0
q.append((r1,c1, cnt))

impossible = True

while q : 
    r,c, cnt= q.popleft()

    if r==r2 and c==c2:
        impossible = False
        print(cnt); exit()

    for i in range(4) :
        tmpr = r+x[i] ; tmpc = c+y[i]
        if 0<=tmpr<10 and 0<=tmpc<9 and mapp[tmpr][tmpc]!=2  :
            for j in range(i*2, i*2+2) : 
                tmpr+=xx[j] 
                tmpc+=yy[j]
                
                if 0<=tmpr<10 and 0<=tmpc<9 and mapp[tmpr][tmpc]!=2  :
                    mapp[tmpr][tmpc]=2
                    q.append((tmpr, tmpc, cnt+1))

if r!=r2 or impossible : 
    print(-1)
