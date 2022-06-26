import sys
from itertools import combinations

n = int(sys.stdin.readline().rstrip())
s = list(map(int,sys.stdin.readline().rstrip().split()))

sums = []
for i in range(1,n+1) :
    combi=list(combinations(s,i)) #i는 1,2,3 으로 증가해나감
    # combi의 생김새
    # i가 1 : [(5,), (1,), (2,)]
    # i가 2 : [(5, 1), (5, 2), (1, 2)]
    # i가 3 : [(5, 1, 2)]
    for i in combi :
        sums.append(sum(i))

sums=sorted(set(sums)) 
# 부분수열 합의 모든 경우 (중복 없이, 오름차순 정렬)

start = 1 #자연수 중 sums에 없는 것

for i in sums : 
    print(i, start)
    if i!=start : # start는 1부터 하나씩 올라가는 아이
        # 부분 합에 속하는 i가 start와 다르다면 , 그 순간의
        # start가 부분합에 속하지 않는 최소의 아이 
        break
    else : start+=1 # 1부터 2,3,4, ... 올라감 

print(start)
