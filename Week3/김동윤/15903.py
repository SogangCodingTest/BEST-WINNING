from calendar import c
import heapq
import sys
# 카드 n장
# m 번의 합체

n, m = map(int,sys.stdin.readline().rstrip().split())

card = []

# 3 2 6 형태로 ~ 
lis = list(map(int, sys.stdin.readline().rstrip().split()))
for i in range(n) : # 카드 heap 에 담기
    heapq.heappush(card, lis[i] )

for i in range(m) : #게임 스타트

    # n장의 카드에 쓰여있는 수를 모두 더한 값이 이 놀이의 점수
    # 이 점수를 가장 작게 만들기
    # 가장 작은 수의 카드 두개만 골라주면 되지 (heap의 가장 앞아이)
        
    x = heapq.heappop(card) #1) 가장 작은 수
    y = heapq.heappop(card) #2) 두번째로 작은 수 

    heapq.heappush(card, x+y) # x와 y에 두 합 더한 것으로 대체해서 다시 넣기
    heapq.heappush(card, x+y)

print(sum(card))
