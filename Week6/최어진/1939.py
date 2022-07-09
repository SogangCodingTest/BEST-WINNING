# collections.deque 사용
from collections import deque

# 섬의 개수 N, 다리의 개수 M 입력
N, M = map(int, input().split())

# 다리와 중량에 대한 그래프 표현을 위한 links 리스트
links = [[] for _ in range(N)]

for _ in range(M):
    # A 정점부터 B 정점으로의 간선 가중치 weight 입력
    A, B, weight = map(int, input().split())
    
    # 양방향 연결로 가중치 추가
    links[A - 1].append((B - 1, weight))
    links[B - 1].append((A - 1, weight))

# 시작 정점 A, 목표 정점 B 입력
A, B = map(int, input().split())

# 중량 weight가 주어졌을 때 물품을 옮길 수 있는지의 여부를 반환하는 bfs() 정의
def bfs(weight):
    # 정점 방문 여부 기록 visited 리스트
    visited = [False] * N
    
    # 큐 초기화
    q = deque()

    # 시작 정점에 대한 방문 여부 기록 및 큐에 추가
    visited[A - 1] = True
    q.append(A - 1)

    # 큐가 비어있지 않으면 계속 탐색
    while len(q) > 0:
        # 큐에서 맨 앞 요소(현재 위치한 섬)을 pop
        current = q.popleft()

        # 목표 섬에 도달했을 때 true 리턴
        if current == B - 1:
            return True

        # 목표 섬에 도달하지 못했다면
        for vertex, edge_weight in links[current]:
            # 현재 정점에서 연결된 정점들로 방문 여부 체크 후 큐에 삽입
            if not visited[vertex] and weight <= edge_weight:
                visited[vertex] = True
                q.append(vertex)

    # 탐색을 끝내고 큐가 빈 상태로 True가 리턴되지 않았다면
    # A 정점부터 B 정점까지 weight를 운반할 수 없다는 의미이므로 False 리턴
    return False

# 이분 탐색 초기화
start = 1
end = 10**9
answer = -1

while start <= end:
    middle = (start + end) // 2

    if bfs(middle):
        # 가장 마지막으로 탐색에 성공한 중량 최대값 갱신
        answer = middle
        start = middle + 1
    else:
        end = middle - 1

# 정답 출력
print(answer)