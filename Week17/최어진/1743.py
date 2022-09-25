# sys.stdin.readline() 사용
import sys
# 파이썬 재귀 함수 깊이 세팅
sys.setrecursionlimit(10 ** 5)

# 통로의 세로 길이 N, 가로 길이 M, 음식물 쓰레기의 개수 K 입력
N, M, K = map(int, sys.stdin.readline().rstrip().split())
# dfs를 위한 음식물 쓰레기 지도 및 방문 배열 visited 초기화
garbages = [[False for _ in range(M)] for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

# dfs를 위한 상하좌우 방향 배열 선언
moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]

# 음식물 쓰레기 좌표 입력
for _ in range(K):
    r, c = map(int, sys.stdin.readline().rstrip().split())
    garbages[r - 1][c - 1] = True

# dfs를 위한 함수 선언
def dfs(r, c):
    count = 1
    visited[r][c] = True

    # 현재 위치 기준 복도의 상하좌우를 검사했을 때,
    for dr, dc in moves:
        # 좌표가 지도를 벗어나지 않으면서
        if r + dr >= 0 and r + dr < N and c + dc >= 0 and c + dc < M:
            # 해당 좌표에 쓰레기가 존재하고, 아직 방문하지 않은 쓰레기인 경우
            if garbages[r + dr][c + dc] and not visited[r + dr][c + dc]:
                # 음식물 쓰레기를 뭉친다.
                count += dfs(r + dr, c + dc)

    # 총 합쳐진 음식물 쓰레기의 크기 반환
    return count

# N x M 크기의 복도의 모든 칸을 검사하면서
answer = 0
for i in range(N):
    for j in range(M):
        # 방문하지 않은 쓰레기가 존재한다면
        if garbages[i][j] and not visited[i][j]:
            # dfs 수행
            traversal = dfs(i, j)
            # dfs 수행 결과에 따른 가장 큰 음식물 쓰레기 갱신
            answer = traversal if traversal > answer else answer

# 정답 출력
print(answer)
