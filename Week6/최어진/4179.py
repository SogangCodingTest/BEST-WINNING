# collections.deque 사용
from collections import deque
# sys.stdin.readline() 사용
import sys

# 미로의 행 R, 열 C 입력
R, C = map(int, sys.stdin.readline().rstrip().split())

# 미로 정보 2차원 리스트로 입력
maze = [list(sys.stdin.readline().rstrip()) for _ in range(R)]

# 지훈이와 불에 대한 좌표 초기화
jihoon = None
fires = []

# 미로의 모든 칸을 순회하며 지훈이와 불에 대한 위치를 저장
for i in range(R):
    for j in range(C):
        if maze[i][j] == 'J':
            jihoon = (i, j)
        elif maze[i][j] == 'F':
            fires.append((i, j))

# BFS 방문 기록을 위한 visited 2차원 리스트를 충분히 큰 값으로 초기화
visited = [[10**6 for _ in range(C)] for _ in range(R)]

# 불에 대한 BFS 함수 정의
def bfs_fire():
    global visited

    # 큐 초기화
    q = deque()

    # 초기 미로에 존재하는 불들에 대해서 도달 시간 기록 후 큐에 삽입
    for i, j in fires:
        visited[i][j] = 0
        q.append((i, j, 0))
    
    # 큐가 비어 있지 않을 동안 반복
    while len(q) != 0:
        # 맨 앞 요소(불의 위치..., 도달 시간)을 추출
        i, j, cnt = q.popleft()

        # 불이 갈 수 있는 4개 방향에 대해 조건 검사
        #     조건 1. 미로의 인덱스를 벗어나지 않을 것
        #     조건 2. 막혀 있는 칸(#)이 아닐 것
        #     조건 3. 해당 칸에 불이 붙는 더 짧은 시간을 갱신할 수 있는 경우
        # 위 조건에 부합한다면 해당 칸에 대해 방문 기록 후 큐에 삽입
        if i > 0 and maze[i - 1][j] != '#' and visited[i - 1][j] > cnt + 1:
            visited[i - 1][j] = cnt + 1
            q.append((i - 1, j, cnt + 1))
        if i < R - 1 and maze[i + 1][j] != '#' and visited[i + 1][j] > cnt + 1:
            visited[i + 1][j] = cnt + 1
            q.append((i + 1, j, cnt + 1))
        if j > 0 and maze[i][j - 1] != '#' and visited[i][j - 1] > cnt + 1:
            visited[i][j - 1] = cnt + 1
            q.append((i, j - 1, cnt + 1))
        if j < C - 1 and maze[i][j + 1] != '#' and visited[i][j + 1] > cnt + 1:
            visited[i][j + 1] = cnt + 1
            q.append((i, j + 1, cnt + 1))

# 불에 대한 BFS 수행
bfs_fire()

# 지훈이에 대한 BFS 함수 정의
def bfs_jihoon():
    global visited

    # 큐 초기화
    q = deque()

    # 지훈이의 초기 위치 받아옴
    i, j = jihoon

    # 지훈이의 초기 위치 방문 기록하고 큐에 삽입
    visited[i][j] = 0
    q.append((i, j, 0))

    # 큐가 비어 있지 않을 동안 반복
    while len(q) != 0:
        # 맨 앞 요소(지훈이의 위치..., 도달 시간)을 추출
        i, j, cnt = q.popleft()

        # 지훈이가 미로에 가장자리에 위치한 경우 현재 칸에 도달한 시간 + 1을 정답으로 return
        if i == 0 or i == R - 1 or j == 0 or j == C - 1:
            return cnt + 1

        # 지훈이가 갈 수 있는 4개 방향에 대해 조건 검사
        #     조건 1. 막혀 있는 칸(#)이 아닐 것
        #     조건 2. 해당 칸에 기록된 불이 붙는 시간보다 지훈이의 현재 시간이 더 짧은 경우
        # 위 조건에 부합한다면 해당 칸을 큐에 삽입
        # 추가로 고려할 점 : visited[해당 칸]을 cnt + 1로 갱신함으로써
        #               지훈이가 왔던 길을 다시 돌아가는 일이 없게 만듦 (메모리 초과 방지)
        if maze[i - 1][j] != '#' and visited[i - 1][j] > cnt + 1:
            visited[i - 1][j] = cnt + 1
            q.append((i - 1, j, cnt + 1))
        if maze[i + 1][j] != '#' and visited[i + 1][j] > cnt + 1:
            visited[i + 1][j] = cnt + 1
            q.append((i + 1, j, cnt + 1))
        if maze[i][j - 1] != '#' and visited[i][j - 1] > cnt + 1:
            visited[i][j - 1] = cnt + 1
            q.append((i, j - 1, cnt + 1))
        if maze[i][j + 1] != '#' and visited[i][j + 1] > cnt + 1:
            visited[i][j + 1] = cnt + 1
            q.append((i, j + 1, cnt + 1))

    # 만약 큐가 빌 때까지 BFS를 돌렸지만 정답이 반환되지 않았다면
    # 지훈이가 불에 탔다는 의미이므로 -1 return
    return -1

# 지훈이에 대한 BFS 수행
answer = bfs_jihoon()

# 정답 출력
print(answer if answer != -1 else 'IMPOSSIBLE')