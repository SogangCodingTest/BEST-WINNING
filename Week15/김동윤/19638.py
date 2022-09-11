from heapq import heappop, heappush
import math
import sys
# 인구수, 센티의 키, 뿅망치 횟수 제한 
n,h,t = map(int, sys.stdin.readline().split())
giant=[]
use=0
for _ in range(n) :
    target = int(sys.stdin.readline())
    heappush(giant, (-target, target))

for _ in range(t):
    nowminus, now = heappop(giant)

    if abs(now)<h :
        heappush(giant, (-abs(now), abs(now)))
        break

    elif abs(now)==1 : 
        heappush(giant, (-1, 1))
        break

    else : 
        heappush(giant, (-1*(abs(now)//2),abs(now)//2))
        use+=1

if giant[0][1] >= h:
    print("NO")
    print(giant[0][1])

else : 
    print("YES")
    print(use)
