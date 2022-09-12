from collections import deque
import sys
k=int(sys.stdin.readline().strip())

def bfs(start) :    
    q=deque()
    q.append(start)
    visit[start]=2 # 처음은 2 
    while q :
        now = q.popleft()
        
        for chk in graph[now]:
            if visit[chk]==-1 : 
                q.append(chk)
                visit[chk] = -visit[now] 

                # 지금 아이와 반대 색깔로 넣어주기
            else : 
                if visit[chk]==visit[now] :
                    return False
    return True

for test in range(k) :

    v,e = map(int, sys.stdin.readline().strip().split())
    graph = [[] for _ in range(v+1)]
    visit = [-1 for _ in range(v+1)]
    possible = True
    for _ in range(e) :
        u,v = map(int, sys.stdin.readline().strip().split())
        graph[u].append(v)
        graph[v].append(u)
    
    for i in range(1,v+1) : 
        if visit[v]==-1 : 
            possible = bfs(i)
        if possible==False:
            break
    if possible : print("YES")
    else : print("NO")
