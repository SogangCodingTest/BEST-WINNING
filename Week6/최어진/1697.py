# collections.deque 사용
from collections import deque

# 수빈의 현재 위치와 동생의 위치 입력
subin, sister = map(int, input().split())

# 큐 선언 후 수빈의 현재 위치 삽입
q = deque()
q.append([subin, 0])

# bfs를 위한 함수 정의
def bfs():
    # 수빈의 방문 위치 기록을 위한 visited 리스트 초기화
    visited = [False] * 100001

    # 큐가 비어있지 않으면 계속 탐색
    while len(q) > 0:
        # 큐에서 맨 앞 요소(수빈의 위치, 이동 횟수)를 pop
        moved_subin, level = q.popleft()        

        # 동생 찾았을 경우 이동 횟수 return
        if moved_subin == sister :
            return level

        ####################
        # 동생을 찾지 못했을 경우
        ####################

        # 수빈의 현재 위치를 visited에 기록
        visited[moved_subin] = True

        # 수빈이 다음 이동할 수 있는 위치를 검사 후, 방문하지 않았다면 큐에 추가
        if moved_subin + 1 <= 100000 and not visited[moved_subin + 1] :
            q.append([moved_subin + 1, level + 1])
        if moved_subin - 1 >= 0 and not visited[moved_subin - 1] :
            q.append([moved_subin - 1, level + 1])
        if moved_subin * 2 <= 100000 and not visited[moved_subin * 2] :
            q.append([moved_subin * 2, level + 1])

# bfs 탐색 진행
answer = bfs()

# 정답 출력
print(answer)