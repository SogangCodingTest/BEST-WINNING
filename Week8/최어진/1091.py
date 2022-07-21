# sys.stdin.readline() 사용
import sys

# 카드의 개수 N 입력
N = int(sys.stdin.readline().rstrip())

# (현재 레인에 놓인) 원래 각자 도달해야 할 플레이어 정보를 나타낸 카드들의 정보 P 입력
P = list(map(int, sys.stdin.readline().rstrip().split()))

# i 레인에 놓인 카드가 S(i) 레인으로 놓이게 되는 섞는 방법을 나타낸 S 입력
S = list(map(int, sys.stdin.readline().rstrip().split()))

# 1. 앞에 위치한 레인 0부터 레인 2까지 P의 순서로 카드를 놓는다. (이미 놓여져 있음)
cards = P.copy()
# 섞은 횟수를 기록하는 카운트 변수 초기화
cnt = 0

while True:
    # 레인 0부터 레인 N까지 놓인 카드에 대해서 조건 검사
    finished = True
    cycle = True
    for i in range(N):
        # 2. 놓인 카드가 0 1 2 0 1 2 ... 의 순서인지 검사
        if cards[i] != i % 3:
            finished = False
        # 3. 놓인 카드가 P와 같은 순서인지 검사
        if cards[i] != P[i]:
            cycle = False
    
    # 카드를 목표대로 섞었다면, 섞기를 중단하고 나누어 준다.
    if finished:
        break

    # 카드 섞기에 사이클이 발생했다면, 섞기를 중단하고 -1을 출력한다.
    if cnt > 0 and cycle:
        cnt = -1
        break

    # 그렇지 않다면,
    new_cards = cards.copy()
    for idx in range(N):
        # 카드를 방법 S에 따라 섞는다.
        new_cards[S[idx]] = cards[idx]

    cards = new_cards

    # 섞은 횟수를 1 누적한다.
    cnt += 1

# 정답 출력
print(cnt)