from collections import deque

subin, sister = map(int, input().split())

q = deque()
q.append([subin, 0])

def bfs():
    visited = [False] * 100001
    answer = 100001

    while len(q) > 0:
        moved_subin, level = q.popleft()        

        # 동생 찾음?
        if moved_subin == sister :
            return level

        # 현재 위치 방문 기록
        visited[moved_subin] = True

        # 동생 못 찾았다면...
        if moved_subin + 1 <= 100000 and not visited[moved_subin + 1] :
            q.append([moved_subin + 1, level + 1])
        if moved_subin - 1 >= 0 and not visited[moved_subin - 1] :
            q.append([moved_subin - 1, level + 1])
        if moved_subin * 2 <= 100000 and not visited[moved_subin * 2] :
            q.append([moved_subin * 2, level + 1])

answer = bfs()

print(answer)