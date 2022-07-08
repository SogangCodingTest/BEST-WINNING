# collections.deque 사용
from collections import deque
# exit() 사용
import sys

# 토마토 상자의 가로 M, 세로 N, 쌓여진 높이 H 입력
M, N, H = map(int, input().split())

# 익은 토마토, 안 익은 토마토, 그리고 빈 칸에 대한 정보 tomatoes 3차원 리스트 입력
tomatoes = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

# 토마토에 대한 BFS 방문 여부 visited 3차원 리스트로 초기화
visited = [[[999999 for _ in range(M)] for _ in range(N)] for _ in range(H)]

# 큐 초기화
q = deque()

# 익지 않은 토마토들을 큐에 추가 및 visited 0으로 입력
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomatoes[i][j][k] == 1:
                visited[i][j][k] = 0
                q.append([i, j, k, 0])

# 큐가 비어 있지 않은 동안 BFS 진행
while len(q) > 0:
    # 큐에서 뺀 요소에서 높이, 세로, 가로 순으로 인덱싱 변수 i, j, k로 받음
    # 동시에 해당 칸의 토마토가 익기까지 걸린 날 수를 day로 받음
    i, j, k, day = q.popleft()

    # 해당 토마토가 영향을 줄 수 있는 상/하/죄/우/왼쪽/오른쪽 토마토들에 대해 조건 검사 후 큐에 삽입
    # 조건 검사하는 내용은
    #     1. 인덱싱 범위 내에 있을 것
    #     2. 해당 칸이 비어 있지 않을 것 (!= -1)
    #     3. 해당 칸의 토마토에 대한 기존의 익기까지의 날짜보다
    #         새로 비교하는 익기까지의 날짜가 더 짧을 경우 BFS를 통해 갱신하도록 함
    if 0 < i and tomatoes[i - 1][j][k] != -1 and visited[i - 1][j][k] > day + 1:
        visited[i - 1][j][k] = day + 1
        q.append([i - 1, j, k, day + 1])
    if i < H - 1 and tomatoes[i + 1][j][k] != -1 and visited[i + 1][j][k] > day + 1:
        visited[i + 1][j][k] = day + 1
        q.append([i + 1, j, k, day + 1])

    if 0 < j and tomatoes[i][j - 1][k] != -1 and visited[i][j - 1][k] > day + 1:
        visited[i][j - 1][k] = day + 1
        q.append([i, j - 1, k, day + 1])
    if j < N - 1 and tomatoes[i][j + 1][k] != -1 and visited[i][j + 1][k] > day + 1:
        visited[i][j + 1][k] = day + 1
        q.append([i, j + 1, k, day + 1])

    if 0 < k and tomatoes[i][j][k - 1] != -1 and visited[i][j][k - 1] > day + 1:
        visited[i][j][k - 1] = day + 1
        q.append([i, j, k - 1, day + 1])
    if k < M - 1 and tomatoes[i][j][k + 1] != -1 and visited[i][j][k + 1] > day + 1:
        visited[i][j][k + 1] = day + 1
        q.append([i, j, k + 1, day + 1])

#-------------------------------#
#--- BFS를 끝내고 큐가 비워진 시점 ---#
#-------------------------------#

answer = 0

for i in range(H):
    for j in range(N):
        for k in range(M):
            # 전체 토마토 상자 중 맨 처음 익지 않은 토마토들에 대해서만 검사
            if tomatoes[i][j][k] == 0:
                # 만약 익지 않은 토마토인데 초기값 그대로 남아 있는 경우는 특정 토마토가 익을 수 없는 상황으로 가정
                if visited[i][j][k] == 999999:
                    print(-1)
                    sys.exit()

                # 익는 데 좀 더 오래 걸리는 토마토를 발견 시 answer를 해당 토마토의 day로 큰 값 비교해서 갱신
                answer = visited[i][j][k] if visited[i][j][k] > answer else answer

# 정답 출력
print(answer)