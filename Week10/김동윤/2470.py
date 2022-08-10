import sys
# 특성값이 0에 가장 가까운 용액을 
# 만들어내는 두 용액을 찾는 프로그램
# 산성은 양수, 알칼리는 음수
n = int(sys.stdin.readline().strip())
lis = list(map(int, sys.stdin.readline().rstrip().split()))
lis.sort() ; minim = 1000000000000001 ; result=[]

s,e = 0,n-1
while s<e : 
    #print(s,e,minim,result)
    cmp = lis[s] + lis[e]

    if lis[s]<0 and lis[e]<0 : # 음음 
        if abs(lis[e]+lis[s])<minim : 
            minim = abs(lis[e]+lis[s])
            result=[]; 
            result.append(lis[s]); 
            result.append(lis[e])
        s+=1

    elif lis[s]>0 and lis[e]>0 : # 양양
        if abs(lis[e]+lis[s])<minim : 
            minim = abs(lis[e]+lis[s])
            result=[]; 
            result.append(lis[s]); 
            result.append(lis[e])
        e-=1

    else : # 음양 
        if abs(lis[e]+lis[s])<minim : 
            minim = abs(lis[e]+lis[s])
            result=[]; 
            result.append(lis[s]); 
            result.append(lis[e])

        
        if cmp>0 : e-=1 # 0에 가까워야 하니깐 더한 값이 양수였으면 좀 줄이자 
        else : s+=1 # 음수였다면 늘리자 

result.sort()
for i in result : 
    print(i, end=" ")
