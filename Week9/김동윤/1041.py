import sys
n = int(sys.stdin.readline().strip())
dice = list(map(int, (sys.stdin.readline().strip()).split()))

# 총 세개, 두개 , 한개 이음면 후보들을 각 구해서 가장 작은애가 대표
oned = min(dice)
#############################
twod_candidates = [
    [0,4], [0,1], [0,3], [0,2],
    [1,2], [1,3], [1,5],
    [2,5], [2,4],
    [3,4], [3,5], # (3,5) 와 (4,5) 경우를 누락했었다;; 
    [4,5]
]
twod = 100000001
for x,y in twod_candidates:
    if twod > dice[x]+dice[y] :
        twod = dice[x]+dice[y]
################################
three_candidates = [
    [0,1,2], [0,2,4],[0,3,4], [0,1,3],
    [5,2,1], [5,2,4], [5,4,3], [5,1,3]
]
threed = 100000001
for x,y,z in three_candidates:
    if threed > dice[x]+dice[y]+dice[z] :
        #print(x,y,z, dice[x]+dice[y]+dice[z])
        threed =  dice[x]+dice[y]+dice[z] 
#################################

if n==1 : 
    maxn = max(dice)
    print(sum(dice)-maxn)
else :  # 2~
    top = threed*4 + twod*((n-2)*4) + oned*((n-2)*(n-2))
    common = twod*4 + oned*((n-2)*4)
    print(top + common*(n-1))
