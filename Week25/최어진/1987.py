from collections import deque
import sys

input = sys.stdin.readline

R, C = map(int, input().rstrip().split())

board = [list(input().rstrip()) for _ in range(R)]

q = deque()
visited = 1 << (ord(board[0][0]) - ord('A'))
q.append((0, 0, visited, 1))

moves = ((0, 1), (0, -1), (1, 0), (-1, 0))

answer = -1

while q:
    r, c, visited, level = q.popleft()

    answer = max(answer, level)

    for dr, dc in moves:
        if 0 <= r + dr < R and 0 <= c + dc < C:
            if not (visited & (1 << (ord(board[r + dr][c + dc]) - ord('A')))):
                q.append((r + dr, c + dc, visited ^ (1 << (ord(board[r + dr][c + dc]) - ord('A'))), level + 1))

    # print(q)

print(answer)
