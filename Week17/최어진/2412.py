# 문제 풀이에 고민한 요소
# 1. 최소 이동 횟수를 업데이트해야 하므로 visited 배열이 필요한 와중에, 모든 요소에 대해 만들기 너무 큰 크기인 경우 처리 방법?
# 2. BFS를 수행한다고 했을 때 시간 복잡도가 아슬아슬한데 이를 이분 탐색으로 처리할 수 있는 테크닉?

import sys
from collections import deque

n, T = map(int, sys.stdin.readline().rstrip().split())

graph = {}
for _ in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split())

    if y in graph.keys():
        graph[y].append(x)
    else:
        graph[y] = [x]

# graph.sort(key=lambda d: (d[0], d[1]))

q = deque()
q.append([0, 0, 0])

goal = False
while len(q) != 0:
    x, y, level = q.popleft()

    if y == T:
        goal = True
        break

    for dx in range(x - 2, x + 3, 1):
        for dy in range(y - 2, y + 3, 1):

            if dy in graph.keys() and dx in graph[dy]:
                graph[dy].remove(dx)
                q.append([dx, dy, level + 1])

if goal:
    print(level)
else:
    print(-1)
