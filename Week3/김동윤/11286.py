import sys
import heapq

lis = []

n = int(sys.stdin.readline().rstrip())

for i in range(n) :
    # [(1, -1), (1, -1), (1, 1), (1, 1), (2, 2)]
    # [(1, -1), (1, -1), (1, 1), (1, 1), (2, 2), (2, -2)]       
    x = int(sys.stdin.readline().rstrip())

    # 만약 x가 0이 아니라면 
    # 배열에 x라는 값을 넣는(추가하는) 연산
    if x!=0 :
        if x<0:
            absx = -x #음수라면 절댓값은 음수 붙여야 함 
        else : absx = x #양수라면 절댓값은 그대로 
        heapq.heappush(lis, (absx, x)) #절댓값, 본래 값으로 저장되게 함 

    # x가 0이라면 배열에서 
    # 절댓값이 가장 작은 값을 출력하고 그 값을 배열에서 제거하는 경우
    else : 
        if not lis :
            print(0)
        else : 
            target = heapq.heappop(lis)
            print(target[1])
                

