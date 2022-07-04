import sys

n,m = map(int, sys.stdin.readline().rstrip().split())
map = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
cnt = 0 # 그림의 갯수
rdis = [ 1, -1, 0, 0]
cdis = [0, 0 , 1, -1]

def dfs(r,c) :
    global visited, big

    for i in range(4) :
        tmpr = r+rdis[i]
        tmpc = c+cdis[i]

        if 0<=tmpr<n and \
            0<=tmpc<m and \
                visited[tmpr][tmpc]==0 and \
                    map[tmpr][tmpc]==1 :

            big+=1
            visited[tmpr][tmpc] = 1
            dfs(tmpr,tmpc)

maxarea = 0 # 넓은 그림의 넓이

for i in range(n) :
    for j in range(m) :
        if(map[i][j]==1 and visited[i][j]==0) :
            cnt+=1 #그림 발견 (그림 갯수 갱신)
            big = 1
            visited[i][j] = 1
            dfs(i,j)
            if big > maxarea :
                maxarea = big

print(cnt)
print(maxarea)
