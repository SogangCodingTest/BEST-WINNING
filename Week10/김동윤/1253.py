from collections import Counter
import sys

n = int(sys.stdin.readline().strip())
# N개의 수 중에서 어떤 수가 
# 다른 수 두 개의 합으로 나타낼 수 있다면 
# 그 수를 “좋다(GOOD)”
lis = list(map(int, sys.stdin.readline().rstrip().split()))
lis.sort()
res = 0
for i in range(n) :
    s,e = 0, n-1
    target = lis[i]
    while s<e : 
        cmp = lis[s] + lis[e]
        if cmp < target : # cmp가 더 작다면 키워야지 
            s+=1 
        
        elif cmp == target : 
            # 나를 제외한 두수 여야 하므로, 내가 거리면 예외처리
            if s==i : s+=1 
            elif e==i : e-=1
            else : 
                res+=1
                break

        else : e-=1 # cmp가 더 크다면 줄여야지 

print(res)
