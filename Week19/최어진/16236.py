# 백준 16236번 : 아기 상어

# 전략

# 코드

from collections import deque
import sys

def input(): return sys.stdin.readline().rstrip()

# 그래프 구성
N = int(input())
graph = list(list(map(int, input().split())) for _ in range(N))

# 상하좌우 방향 초기화
direction = ((-1, 0), (1, 0), (0, -1), (0, 1))

# 최단 거리를 위한 초기화 값
INF = 1e9

# 아기 상어 크기
shark_size = 2

# 아기 상어의 현재 좌표
now_x, now_y = 0, 0

# 아기 상어 초기 위치 확인
for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            now_x, now_y = i, j
            graph[i][j] = 0

# 현재 위치에서 각 물고기까지의 거리를 반환, 지나는 경로마다 값을 저장
def BFS():
    q = deque([(now_x, now_y)])
    # 방문 여부
    visited = [[-1] * N for _ in range(N)]
    visited[now_x][now_y] = 0

    while q:
        x, y = q.popleft()

        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            # graph 범위 확인
            if 0 <= nx < N and 0 <= ny < N:
                # 상어가 이동 가능한지 확인
                if shark_size >= graph[nx][ny] and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
                    
    return visited

# 먹을 물고기 찾기
def solve(visited):
    x, y = 0, 0
    min_distance = INF
    for i in range(N):
        for j in range(N):
            # BFS에서 지나지 않는 경로는 최단 경로가 아님 + 아기 상어가 먹을 수 있는지 확인
            if visited[i][j] != -1 and 1 <= graph[i][j] < shark_size:
                if visited[i][j] < min_distance:
                    min_distance = visited[i][j]
                    x, y = i, j

    # 모두 탐색해도 그대로 INF이면 먹을 물고기가 없다는 것
    if min_distance == INF:
        return False
    else:
        return x, y, min_distance

answer = 0
food = 0

while True:
    result = solve(BFS())

    if not result:
        print(answer)
        break
    else:
        last_x, last_y, move = result
        now_x, now_y = last_x, last_y
        # 아기 상어가 이동한 거리 누적
        answer += move
        # 먹은 물고기에 대해 비워주는 처리
        graph[now_x][now_y] = 0
        # 먹은 횟수 1 추가
        food += 1

    # 상어의 크기가 커질 수 있는 경우
    if food >= shark_size:
        shark_size += 1
        food = 0