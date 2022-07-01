from collections import deque
import sys
sys.setrecursionlimit(10**6)

n,m = map(int, sys.stdin.readline().rstrip().split())
map = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

cnt = 0 # 그림의 갯수

rdis = [ 1, -1, 0, 0]
cdis = [0, 0 , 1, -1]

def bfs(q) :
    global big
    while q : 
        now = q.popleft()
        for i in range(4) :
            tmpr = now[0]+rdis[i]
            tmpc = now[1]+cdis[i]

            if 0<=tmpr<n and \
                0<=tmpc<m and \
                    visited[tmpr][tmpc]==0 and \
                        map[tmpr][tmpc]==1 : 
                # 범위에서 안 벗어나고 , 안 방문했고, 1이라면
                big+=1 # 그림 크기 증가시키기 
                visited[tmpr][tmpc] = 1
                q.append((tmpr,tmpc))
    return big

maxarea = 0 # 넓은 그림의 넓이
q=deque()
for i in range(n) :
    for j in range(m) :
        if(map[i][j]==1 and visited[i][j]==0) :
            q.append((i,j)) # 큐에 해당 좌표 집어넣어 
            cnt+=1 # 그림 발견 (그림 갯수 갱신)
            big = 1 # 그림의 크기 
            visited[i][j] = 1
            maxarea = max(maxarea, bfs(q)) # 기존 큰 그림 vs 지금 그림 크기 

print(cnt)
print(maxarea)
