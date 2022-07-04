import sys
sys.setrecursionlimit(10**5)
# sys.setrecursionlimit(10**9) : 로 하면 에러난다.

n = int(sys.stdin.readline().rstrip()) # 노드의 갯수 

node = [[] for _ in range(n+1)] # 1부터 시작
dis = [0 for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

def dfs(num) : # 각 노드들과 루트 노트(1) 사이의 거리 구하는 dfs
        visited[num] = 1
        for child in node[num] :
            if visited[child]==0 :
                dis[child] = dis[num]+1
                dfs(child)

for i in range(n-1) : 
    a, b= map(int, sys.stdin.readline().rstrip().split())
    node[a].append(b) ; node[b].append(a)

dfs(1) # 루트  노드부터 -> 이 친구와 다른 노드 사이의 측정 위해

total = 0
possible = False

for j in range(2, len(node)) :
    if(len(node[j])==1) :
        total+=(dis[j]) # 리프에서 루트까지의 총 거리 구함 

# 리프에서 루트까지 가는 총거리가 홀수면, 
# 짝수번때 형석은 말이 없으니 지게 됨

if (total%2==1) : print("Yes") 
else : print("No")
