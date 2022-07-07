from collections import deque
import pprint

# 섬의 개수 N, 다리의 개수 M 입력
N, M = map(int, input().split())

# 다리와 중량에 대한 그래프 표현을 위한 links 리스트
links = [[] for _ in range(N)]

for _ in range(M):
    A, B, weight = map(int, input().split())
    
    # 양방향 연결 관계 및 가중치 추가
    links[A - 1].append((B - 1, weight))
    links[B - 1].append((A - 1, weight))

start, end = map(int, input().split())

visited = [0] * N
visited[start - 1] = 1

# 큐 선언 후 시작 섬의 위치 삽입
q = deque()
q.append([start - 1, visited.copy(), 10**9])

# bfs를 위한 함수 정의
def bfs():
    global end

    answer = -1

    # 큐가 비어있지 않으면 계속 탐색
    while len(q) > 0:
        # 큐에서 맨 앞 요소(현재 위치한 섬, 방문 기록 리스트, 최대 중량)를 pop
        current, visited, max_weight = q.popleft()        

        # 목표 섬에 도달한 한 가지 방법 찾았을 때 -> 그 때까지의 최대 중량 비교해서 갱신
        if current == end - 1:
            answer = max_weight if answer < max_weight else answer
            continue

        #########################
        # 목표 섬에 도달하는 과정인 경우
        #########################

        # 수빈의 현재 위치를 visited에 기록

        for node, weight in links[current]:
            if visited[node] == 0:
                new_visited = visited.copy()
                new_visited[node] = 1
                q.append([node, new_visited, weight if max_weight > weight else max_weight])

    return answer

answer = bfs()

print(answer)