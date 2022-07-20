# collections.deque 사용
from collections import deque
# sys.stdin.readline() 사용
import sys

# 상의 세로 위치 sang_r, 가로 위치 sang_c 입력
sang_r, sang_c = map(int, sys.stdin.readline().rstrip().split())
# 왕의 세로 위치 wang_r, 가로 위치 wang_c 입력
wang_r, wang_c = map(int, sys.stdin.readline().rstrip().split())

# 상이 다음에 이동할 수 있는 8개 방향에 대한
# 11시 방향부터 시계 방향으로 돌아가는 offset 리스트 정의
direction = [[-3, -2], [-3, 2], [-2, 3], [2, 3], [3, 2], [3, -2], [2, -3], [-2, -3]]

# 상이 direction[i]번째 방향으로 이동할 때 검사해야 할
# 왕이 존재해서는 안 되는 좌표들의 offset 리스트 정의
wang_direction =\
    [[[-1, 0], [-2, -1]],\
    [[-1, 0], [-2, 1]],\
    [[0, 1], [-1, 2]],\
    [[0, 1], [1, 2]],\
    [[1, 0], [2, 1]],\
    [[1, 0], [2, -1]],\
    [[0, -1], [1, -2]],\
    [[0, -1], [-1, -2]]]

# BFS 방문을 기록하기 위한 visited 리스트를 충분히 큰 값으로 초기화
visited = [[99999 for _ in range(9)] for _ in range(10)]

# 빈 큐 선언
q = deque()

# 상의 초기 위치를 visited에 기록하고 큐에 추가
visited[sang_r][sang_c] = 0
q.append((sang_r, sang_c, 0))

# BFS를 위한 함수 정의
def bfs():
    # 큐가 비어 있지 않을 동안 반복
    while len(q) != 0:
        # 상의 세로 위치 y, 가로 위치 x, 이동 횟수 cnt 큐에서 추출
        y, x, cnt = q.popleft()

        # 상이 왕에 도달했다면
        if y == wang_r and x == wang_c:
            # 이동 횟수 출력하고 BFS 종료
            return cnt

        ##########################################
        ########## 상이 왕에 도달하지 않았다면 ##########
        ##########################################

        # 이동할 수 있는 8개 방향에 대해 장기 판을 벗어나지 않는 경우만 필터링
        moves = ((i, h, w) for i, (h, w) in enumerate(direction) if y + h >= 0 and y + h < 10 and x + w >= 0 and x + w < 9)

        # 장기판 내에서 이동할 수 있는 방향들에 대해서 처리
        for i, h, w in moves:
            # 해당 이동할 수 있는 방향으로의 경로 상에 왕이 존재하는지 검사
            wang_on_route = False
            for wang_y, wang_x in wang_direction[i]:
                # 만약 경로 상에 왕이 존재한다면,
                if y + wang_y == wang_r and x + wang_x == wang_c:
                    # 해당 경로로로는 BFS 탐색을 수행하지 않음
                    wang_on_route = True
                    break

            if wang_on_route: continue

            # 해당 칸에 방문했던 이전 기록보다 최단 거리를 갱신할 수 있다면
            if visited[y + h][x + w] > cnt + 1:
                # 해당 칸의 최단 거리를 갱신하고 큐에 추가
                visited[y + h][x + w] = cnt + 1
                q.append((y + h, x + w, cnt + 1))

    # 만약 큐가 비었는데도 return 값이 발생하지 않았다면
    # 상이 왕에게 도달할 수 있는 방법이 없다고 판단하고 -1 return
    return -1

# BFS 수행
answer = bfs()

# 정답 출력
print(answer)