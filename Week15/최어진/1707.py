import sys
sys.setrecursionlimit(10 ** 6)
from collections import deque

test_case = int(sys.stdin.readline())

for _ in range(test_case):
    V, E = map(int, sys.stdin.readline().rstrip().split())

    graph = [[] for _ in range(V)]
    visited = [False for _ in range(V)]

    # 그래프의 연결 정보 E개 입력
    for _ in range(E):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        if b - 1 not in graph[a - 1]:
            graph[a - 1].append(b - 1)
            graph[b - 1].append(a - 1)

    flag = True
    for i, vis in enumerate(visited):
        if not vis:
            if not dfs(i, 1):
                break

    print('YES' if flag else 'NO')
    