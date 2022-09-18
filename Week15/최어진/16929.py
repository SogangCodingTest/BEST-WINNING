# sys.stdin.readline 이용
import sys

# 게임판의 세로 크기 N, 가로 크기 M 입력
N, M = map(int, sys.stdin.readline().split())

# 게임판 정보 board 입력 및 방문 기록 배열 visited 초기화
board = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

# 문제 풀이 전략
# 1. 게임판의 방문하지 않은 점을 발견 시 해당 점으로부터 DFS 시작
# 2-1.    같은 모양이면서 방문하지 않은 점을 만나면 -> DFS 계속 이어감
# 2-2.    같은 모양이면서 방문한 점을 만나면 -> 방문 횟수 차이가 3 이상이면 answer를 True로 체크
# 3. DFS가 모두 종료된 후에 1로 반복
# 4. 게임판의 모든 점을 방문한 후 answer 값에 따라 정답 출력
# [포인트] 꼭 사이클이 직사각형 모양일 필요는 없다는 것

# 정답 플래그 초기화
answer = False

# DFS 함수 선언
def dfs(i, j, level, mark):
    global answer

    # 위 방향으로의 DFS
    if i - 1 >= 0:
        # 같은 모양이면서,
        if board[i - 1][j] == mark:
            # 방문하지 않은 경우,
            if not visited[i - 1][j]:
                # 해당 점에 방문 여부를 체크하고 DFS 수행
                visited[i - 1][j] = level + 1
                dfs(i - 1, j, level + 1, mark)
            # 적어도 3번 전에 방문한 적이 있는 경우,
            elif level - visited[i - 1][j] >= 3:
                # 사이클이 있다고 체크
                answer = True
    # 아래 방향으로의 DFS
    if i + 1 < N:
        # 같은 모양이면서,
        if board[i + 1][j] == mark:
            # 방문하지 않은 경우,
            if not visited[i + 1][j]:
                # 해당 점에 방문 여부를 체크하고 DFS 수행
                visited[i + 1][j] = level + 1
                dfs(i + 1, j, level + 1, mark)
            # 적어도 3번 전에 방문한 적이 있는 경우,
            elif level - visited[i + 1][j] >= 3:
                # 사이클이 있다고 체크
                answer = True
    # 왼쪽 방향으로의 DFS
    if j - 1 >= 0:
        # 같은 모양이면서,
        if board[i][j - 1] == mark:
            # 방문하지 않은 경우,
            if not visited[i][j - 1]:
                # 해당 점에 방문 여부를 체크하고 DFS 수행
                visited[i][j - 1] = level + 1
                dfs(i, j - 1, level + 1, mark)
            # 적어도 3번 전에 방문한 적이 있는 경우,
            elif level - visited[i][j - 1] >= 3:
                # 사이클이 있다고 체크
                answer = True
    # 오른쪽 방향으로의 DFS
    if j + 1 < M:
        # 같은 모양이면서,
        if board[i][j + 1] == mark:
            # 방문하지 않은 경우,
            if not visited[i][j + 1]:
                # 해당 점에 방문 여부를 체크하고 DFS 수행
                visited[i][j + 1] = level + 1
                dfs(i, j + 1, level + 1, mark)
            # 적어도 3번 전에 방문한 적이 있는 경우,
            elif level - visited[i][j + 1] >= 3:
                # 사이클이 있다고 체크
                answer = True

# 게임판 내의 방문하지 않은 점이 있는지 검사
while True:
    all_visited = True
    for i in range(N):
        for j in range(M):
            # 방문하지 않은 점을 발견하면
            if not visited[i][j]:
                all_visited = False
                # 해당 점에 방문 여부를 체크하고 DFS 수행
                visited[i][j] = 1
                dfs(i, j, 1, board[i][j])

    # 이미 사이클을 찾았거나, 모든 점을 방문했으면, 반복문 탈출
    if answer or all_visited: break

# 정답 출력
print('Yes' if answer else 'No')