# collections.deque 사용
from collections import deque

# 전체 층 수 F, 현재 위치 S, 목적 층 G, 증가 값 U, 감소 값 D 입력
F, S, G, U, D = map(int, input().split())

# 큐 선언 후 시작 층 삽입
q = deque()
q.append([S, 0])

# bfs를 위한 함수 정의
def bfs():
    # 층 수 방문 위치 기록을 위한 visited 리스트 초기화
    visited = [False] * F # 1 ~ F (최대 1,000,000)
    answer = -1

    # 큐가 비어있지 않으면 계속 탐색
    while len(q) > 0:
        # 큐에서 맨 앞 요소(현재 층 수, 버튼 누른 횟수)를 pop
        current, cnt = q.popleft()

        # 이미 방문한 층이면 넘어가기
        if visited[current - 1]:
            continue

        # 목적 층에 도착했을 시 버튼 누른 횟수 answer에 업데이트하고 while문 bfs 중단
        if current == G:
            answer = cnt
            break

        #############################
        # 아직 해당 층에 도착하지 못했을 경우
        #############################

        # 현재 층의 방문 여부를 visited에 기록
        visited[current - 1] = True

        # U, D 값에 의해 다음 이동할 수 있는 층을 큐에 추가
        if current + U <= F:
            q.append([current + U, cnt + 1])
        if current - D >= 1:
            q.append([current - D, cnt + 1])

    return answer

# bfs 탐색 진행
answer = bfs()

# 정답 출력
print(answer if answer != -1 else "use the stairs")