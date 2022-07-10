# 기본 재귀함수 깊이 10^5로 늘려서 설정
import sys
sys.setrecursionlimit(10**5)

# 트리의 노드 갯수 N 입력
N = int(input())

# 트리의 간선 리스트 초기화
links = [[] for _ in range(N)]

# 간선 정보 입력
for _ in range(N - 1):
    node, link = list(map(int, input().split()))

    # 양방향 그래프로 구성
    links[node - 1].append(link - 1)
    links[link - 1].append(node - 1)

# 총 간선 합산 변수 초기화
total_link_sum = 0

# dfs 중 노드 방문 여부 체크를 위한 visited 리스트 초기화
visited = [False for _ in range(N)]

# dfs 수행을 위한 재귀 함수 정의
def dfs(current_node, link_sum):
    global total_link_sum

    # 현재 도착한 노드의 방문 여부 체크
    visited[current_node] = True
    
    found = False
    for link in links[current_node]:
        # 현재 노드에 연결된 노드 중 방문하지 않은 노드를 골라 dfs 진행
        if not visited[link]:
            found = True
            dfs(link, link_sum + 1)

    # 현재 노드에서 아무 것도 방문할 노드가 없는 경우 리프 노드로 판단
    if not found :
        total_link_sum += link_sum

# 루트 노드부터 dfs 시작
dfs(0, 0)

# 루트 노드부터 각 리프 노드까지의 간선 합이 홀수면 Yes, 짝수면 No 출력
print("Yes" if total_link_sum % 2 == 1 else "No")