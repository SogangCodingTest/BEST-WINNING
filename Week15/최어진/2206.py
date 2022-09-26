import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

board = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]
visited_before = [[999999 for _ in range(M)] for _ in range(N)]
visited_after = [[999999 for _ in range(M)] for _ in range(N)]

q = deque([])

visited_before[0][0] = 1
visited_after[0][0] = 1
q.append([0, 0, 1, True])

found = False

while len(q) != 0:
    i, j, level, chance = q.popleft()

    if i == N - 1 and j == M - 1:
        print(level)
        found = True
        break

    if chance:
        # 위쪽
        if i - 1 >= 0:
            if visited_before[i - 1][j] > level + 1:
                if board[i - 1][j] == 0:
                        visited_before[i - 1][j] = level + 1
                        visited_after[i - 1][j] = level + 1
                        q.append([i - 1, j, level + 1, True])
                else:
                    pass

        # 아래쪽
        if i + 1 < N:
            if board[i + 1][j] == 0:
                if visited[i + 1][j] > level + 1:
                    visited[i + 1][j] = level + 1
                    q.append([i + 1, j, level + 1, chance])
        # 왼쪽
        if j - 1 >= 0:
            if board[i][j - 1] == 0:
                if visited[i][j - 1] > level + 1:
                    visited[i][j - 1] = level + 1
                    q.append([i, j - 1, level + 1, chance])
        # 오른쪽
        if j + 1 < M:
            if board[i][j + 1] == 0:
                if visited[i][j + 1] > level + 1:
                    visited[i][j + 1] = level + 1
                    q.append([i, j + 1, level + 1, chance])

    else:
        pass


    # print(q)

if not found: print(-1)