import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def root_dfs(node,dis): # 기가 노드 찾는 dfs 
    if visited[node]:
        return
    visited[node] = 1 # 방문 처리 
    count = 0 # 내 노드 수 세는 것 (얘가 1이면 여전히 기둥 부분이지)
    nexts = -1 
    for next_node in tree[node]: # 나랑 연결된 노드들 중 
        if not visited[next_node]: # 방문하지 않은 애라면 
            count += 1 # 노드 갯수 세기 
            nexts = next_node
            added_distance = tree[node][next_node]

    if count == 1:
        return root_dfs(nexts,dis+added_distance)

    else: # 노드가 한 개 이상이면 더 이상 기둥 아님
        # 기가노드일때는 재귀 stop, 
        # 지금 노드가 기가노드, 거리 반환 
        return [node,dis]

def leaf_dfs(node,dis): # 리프노드 중 최대 길이 찾는 dfs 
    global leaf_dis
    visited[node] = True

    count = 0 # 노드 수 세주기 
    for next_node in tree[node]:
        if not visited[next_node]:
            leaf_dfs(next_node,dis+tree[node][next_node]) 
            # 다음노드 이동, 가지 길이 갱신 
            count += 1 

    if not count: # 가지 더 뻗을 곳 없삼 (노드가 없다면)
        leaf_dis = max(leaf_dis,dis) # 기존 최댓값이랑 내 가지길이 비교해서 더 큰놈 

################################################################################

n,r = map(int,input().split())
tree = [{} for _ in range(n+1)]
for _ in range(n-1):
    x,y,b = map(int,input().split())
    tree[x][y] = b 
    tree[y][x] = b

visited = [0 for _ in range(n+1)]
root_dis = root_dfs(r,0) 
# 기가노드 찾으면 그때까지의 길이가 기둥이지 

leaf_dis = 0
leaf_dfs(root_dis[0],0)
# 가장 긴 가지 길이 찾기 

print(root_dis[1],leaf_dis)

