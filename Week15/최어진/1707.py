import sys
sys.setrecursionlimit(10 ** 6)

test_case = int(sys.stdin.readline())

def dfs(current, group):
    visited[current] = group

    for neighbor in graph[current]:
        if not visited[neighbor]:
            if not dfs(neighbor, -group):
                return False
        elif visited[neighbor] == group:
            return False

    return True

for _ in range(test_case):
    V, E = map(int, sys.stdin.readline().rstrip().split())

    graph = [[] for _ in range(V)]
    visited = [False for _ in range(V)]

    for _ in range(E):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    for i, vis in enumerate(visited):
        if not vis:
            answer = dfs(i, 1)

    print('YES' if answer else 'NO')
    