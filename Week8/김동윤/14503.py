from collections import deque
import sys
n, m = map(int, sys.stdin.readline().split())
# 북 동 남 서 (북->서->남->동 일케가 왼쪽으로 가는 것임)
# 따라서 -i 해줘야한다. 
r=[-1,0,1,0]
c=[0,1,0,-1]
ror, roc , rdir = map(int, sys.stdin.readline().split())

mapp = []
for i in range(n) : 
    mapp.append(list(map(int,sys.stdin.readline().strip().split())))

q=deque(); q.append((ror,roc,rdir))
cnt = 0

while q:
    curr,curc,curdir = q.popleft()
    # 현재 자리 청소
    if mapp[curr][curc]==0 : 
        mapp[curr][curc]=2 #청소합시다
        cnt+=1

    # 왼쪽 돌면서 탐색 시작 
    for i in range(4) : 
        # 만약 현재 위치가 0 이면(북쪽) = 왼쪽은 서쪽이다
        # 이는 리스트에 [북동남서] 일케 있으므로 인덱스 왼쪽, 즉 일 빼조야해
        # 따라서 북 0 이라면 인덱스 3을 가리켜야 함 
        # 이떄 인덱스 3==-1
        # 0-1-i 일케 해주면 각 위치에 맞게 왼쪽 해당하는 곳 찾아감
        tmpr = curr+r[curdir-1-i] 
        tmpc = curc+c[curdir-1-i]

        if 0<=tmpr<n and 0<=tmpc<m and mapp[tmpr][tmpc]==0: 
            #범위에서 안 벗어나고 청소안된 곳 발견!
                if curdir-1-i<0: 
                    # 방향 넘겨줘야 하는데 -1인 경우 존재,
                    # 북쪽에서 서쪽으로 넘어간 경우는 -1, 
                    # 따라서 4를 더해주면 -1 의 양수 인덱스인 3 ok
                    tmpcurdir=curdir-1-i+4
                else : tmpcurdir=curdir-i-1  
            
                mapp[tmpr][tmpc]=2 #청소합시다
                cnt+=1
                q.append((tmpr, tmpc, tmpcurdir))
                break

        if i==3 : 
            #break 당하지 않고 네 방향 다 돌음;
            #네 방향 모두 벽, 청소완료 경우 -> 캐아스3번
            backr = curr-r[curdir]
            backc = curc-c[curdir]
            if 0<=backr<n and 0<=backc<m and mapp[backr][backc]!=1:
                q.append((backr, backc, curdir))
            else :
                print(cnt)
                exit()
