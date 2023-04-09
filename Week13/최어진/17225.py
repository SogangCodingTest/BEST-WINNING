from collections import deque
import sys

input = sys.stdin.readline

# 상민이가 선물 하나를 포장하는 데 걸리는 시간 A(<= 3 * 10^2)
# 지수가 선물 하나를 포장하는 데 걸리는 시간 B(<= 3 * 10^2)
# 어제 세훈이 가게의 손님 수 N(<= 10^3)
A, B, N = map(int, input().rstrip().split())

q_A = deque()
q_B = deque()

orders = []
for _ in range(N):
    # 주문 시각 T(< 10^5)
    # 선택한 포장지의 색깔 C
    # 주문한 선물의 개수 M(<= 10^2)
    T, C, M = input().rstrip().split()
    
    if C == 'B':
        q_A.append((int(T), int(M)))
    elif C == 'R':
        q_B.append((int(T), int(M)))

# print(q_A)
# print(q_B)

current = 0
answer_A = []
answer_B = []

gift_cnt = 1
A_current, A_cnt = -1, 0
B_current, B_cnt = -1, 0

while True:
    # print(A_current, A_cnt, q_A)
    # print(B_current, B_cnt, q_B)
    # print(answer_A)
    # print(answer_B)
    # print()

    if A_cnt == 0:
        if q_A: A_current, A_cnt = q_A.popleft()
        else: A_current = 999999
    if B_cnt == 0:
        if q_B: B_current, B_cnt = q_B.popleft()
        else: B_current = 999999

    if A_current == 999999 and B_current == 999999: break

    if A_current <= B_current:
        current = A_current
        answer_A.append(gift_cnt)
        gift_cnt += 1

        A_current += A
        A_cnt -= 1
    else:
        current = B_current
        answer_B.append(gift_cnt)
        gift_cnt += 1

        B_current += B
        B_cnt -= 1

print(len(answer_A))
print(" ".join(list(map(str, answer_A))))
print(len(answer_B))
print(" ".join(list(map(str, answer_B))))
