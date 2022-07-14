from collections import deque
import sys

#n개의 섬 
n,m = map(int, sys.stdin.readline().rstrip().split())
bridges=[{} for _ in range(n+1)]
visited = [-1 for _ in range(n+1)]
q=deque()

# 인덱스 n = n번째 섬 이 가지는 (다리, 중량)
for i in range(m) :
    a,b,c=map(int, sys.stdin.readline().rstrip().split())
    if b in bridges[a] :
        if bridges[a][b]<c:
            bridges[a][b]=c
            bridges[b][a]=c

    else : bridges[a][b]=c; bridges[b][a]=c

i1, i2=map(int, sys.stdin.readline().rstrip().split())

print(bridges)

q.append(i1)
visited[i1]=0

while q:
    print(q, visited)
    print()
    now=q.pop()
    
    if now==i2:
        print(visited[i2]);print("yeaaaaaaa")
    for key in (bridges[now]) :
        if visited[key]==-1 :
            visited[key]=max(visited[now],bridges[now][key])
            # 전의 중량 + 나의 중량 
            q.appendleft(key)

# print(visited)
print(visited[i2])
