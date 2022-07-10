# collections.deque 사용
from collections import deque

# L 길이의 시작 이진수 start 입력
start = int('0b' + input().strip(), 2)

# K 길이의 목표 이진수 end 입력
end = int('0b' + input().strip(), 2)

# 큐 선언 후 시작 이진수 삽입
q = deque()
q.append([start, 0])

# bfs를 위한 함수 정의
def bfs():
    # 자연수 생성 기록을 위한 visited 리스트 초기화
    visited = [False] * 1024 # 0 ~ 1023

    # 큐가 비어있지 않으면 계속 탐색
    while len(q) > 0:
        # 큐에서 맨 앞 요소(생성된 이진수)를 pop
        number, level = q.popleft()

        if visited[number]:
            continue

        # 목표 이진수에 도달했을 경우 이동 횟수 return
        if number == end :
            return level

        ############################
        # 목표 이진수에 도달하지 못했을 경우
        ############################

        # 현재 자연수를 visited에 기록
        visited[number] = True

        # 다음 생성할 수 있는 이진수를 검사 후, 이전에 생성한 적이 없다면 큐에 추가
        # 1. 한 자리 숫자를 보수로 바꾸기
        bin_number = bin(number)[2:]
        for i in range(len(bin_number) - 1):
            q.append([number ^ (1 << i), level + 1])
        # 2. 현재 수에 1 더하기
        if number + 1 < 1024:
            q.append([number + 1, level + 1])
        # 3. 현재 수에서 1 빼기
        if number > 0:
            q.append([number - 1, level + 1])

# bfs 탐색 진행
answer = bfs()

# 정답 출력
print(answer)