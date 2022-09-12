# sys.stdin.readline 사용
import sys
# collections.deque 사용
from collections import deque

# 시작 숫자 A, 목표 숫자 B 입력
A, B = map(int, sys.stdin.readline().split())

# 큐 선언 및 초기화
q = deque([])
q.append([A, 1])

# 정답 플래그 초기화
found = False

# 큐가 비어있지 않는 동안 BFS 수행
while len(q) != 0:
    num, level = q.popleft()

    # 목표 숫자에 도달한 경우 출력하고 BFS 종료
    if num == B:
        print(level)
        found = True
        break

    # 첫번째 연산 - 2를 곱한다
    if num * 2 <= B:
        q.append([num * 2, level + 1])
    # 두번째 연산 - 1을 숫자의 오른쪽에 더한다
    if num * 10 + 1 <= B:
        q.append([num * 10 + 1, level + 1])

# BFS를 마무리했을 경우에도 목표에 도달하지 못했다면
if not found:
    # -1 출력하고 종료
    print(-1)
