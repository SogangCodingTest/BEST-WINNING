from collections import deque
import sys
import heapq

n = int(sys.stdin.readline().rstrip())
lis = []
zerocnt = 0

for i in range(n) :
    targ = int(sys.stdin.readline().rstrip())
    if targ!=0:
        heapq.heappush(lis,-1*targ)
    else : # 0이면 
        zerocnt+=1
sum = 0

# 양수만 처리해주는 while 문 
while lis and lis[0]<0: # -1 을 곱해서 저장하기 때문에 양수라면 0보다 작음
    a=heapq.heappop(lis)
    a=-1*a
    # 만약 아직 lis 에 양수가 남아있다면 
    if lis and lis[0]<0: 
        b=heapq.heappop(lis)
        b=-1*b
        # 우선순위 1 : 둘 중에 하나라도 1이면 곱하기보다 더하기가 낫다
        if a == 1 or b == 1 : 
            sum+=(a+b)
        # 우선순위 2 : 둘다 1보다 큰 양수면 곱하기가 낫다. 
        else : 
            sum+=(a*b)
    # 지금 꺼냈던 a가 마지막 양수였다면 그냥 더해주기 
    else : 
        sum+=a

# 이제 음수를 다룰건데 heap-pop으로 하면 
# -5,-4 가 5,4, 로 저장되어있는 상태라 
# 최소힙 특성으로 인해 -5,-4가 나중에 뽑힘 
# 그래서 여기서는 내림차순으로 정렬시켜줌
lis.sort(reverse=True) # 5 4 3 2 1 
lis = deque(lis) # 맨 앞에서부터 뽑을 수 있게 덱으로 바꿔줌

while lis and lis[0]>0:
    a=lis.popleft()
    a=-1*a
    # 1순위 : 다음 음수 있다면 그 음수와 곱해주는 것이 낫다. 
    if len(lis)>0 :
        b=lis.popleft()
        b=-1*b
        sum+=(a*b)
    # 2순위 : 입력으로 0이 들어왔던 게 있으면 0 으로 만들어버리기
    elif zerocnt>0:
        zerocnt-=1
    # 3순위 : 아무것도 없으면 더하는 수 밖에 없다.
    else : 
        sum+=a

print(sum)
