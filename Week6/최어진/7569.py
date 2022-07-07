from collections import deque
import pprint

M, N, H = map(int, input().split())

tomatoes = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

def complete():
    global tomatoes

    for i in range(H):
        for j in range(N):
            for k in range(M):
                if tomatoes[i][j][k] > 0:
                    return False
    
    return True

def bfs():
    global tomatoes

    day = 0
    q = deque()

    for i in range(H):
        for j in range(N):
            for k in range(M):
                if tomatoes[i][j][k] > 0:
                    q.append(i, j, k, 0)

    if len(q) == 0:
        return day

    while len(q) != 0:
        i, j, k, current_day = q.popleft()

        if complete():
            break

        if current_day > day:
            day = current_day

        if 2 < i and tomatoes[i - 1][j][k] != 0:
            tomatoes[i - 1][j][k] -= 1
        if i < 100 and tomatoes[i + 1][j][k] != 0:
            tomatoes[i - 1][j][k] -= 1
        



    return day

answer = bfs()

print(answer)