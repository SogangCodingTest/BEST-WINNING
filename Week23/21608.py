import sys
from collections import defaultdict

dict = defaultdict(int)
n = int(sys.stdin.readline())
mapp = list([0 for _ in range(n+1)] for _ in range(n+1))
member = []
for i in range(n*n) :
    lis = list(map(int, sys.stdin.readline().rstrip().split()))
    dict[lis[0]] = lis[1:]
    member.append(lis[0])

rdis = [-1, 1, 0, 0]
cdis = [0, 0, -1, 1]

for j in range(n*n) : 
    # 좋아하는 학생이 인접한 곳에 가장 많은 애들
    # 여러개면 인접 중 비어있는 칸이 가장 많고
    # 행, 열 번호가 가장 작은 칸 
    
    max_favorite = 0
    max_empty = 0
    maxr = 1
    maxc = 1
    for k in range(1,n+1) :
        for l in range(1,n+1) : 
            if mapp[k][l]==0 : # 비어있으면 인접 4개 검사 시작
                cmp_favorite = 0
                cmp_empty = 0
                for o in range(4) :
                    if( 0<k+rdis[o]<=n and 0<l+cdis[o]<=n) : 
                        if mapp[k+rdis[o]][l+cdis[o]] in dict[member[j] ] :
                            cmp_favorite+=1
                        elif mapp[k+rdis[o]][l+cdis[o]] ==0 :
                            cmp_empty+=1
                            
                if cmp_favorite>max_favorite:
                        maxr = k
                        maxc = l
                        max_favorite = cmp_favorite
                        max_empty = cmp_empty
                    
                elif cmp_favorite==max_favorite and cmp_empty>max_empty :
                        maxr = k
                        maxc = l
                        max_favorite = cmp_favorite
                        max_empty = cmp_empty
                    
                elif cmp_favorite==max_favorite and cmp_empty==max_empty :
                        if k <maxr : 
                            maxr = k
                            maxc = l
                            max_favorite = cmp_favorite
                            max_empty = cmp_empty
                        elif k==maxr and l <maxc : 
                            maxr = k
                            maxc = l
                            max_favorite = cmp_favorite
                            max_empty = cmp_empty
                            
    mapp[maxr][maxc] = member[j]              

total = 0

for k in range(1,n+1) :
    for l in range( 1,n+1) :
        favorite=0
        for o in range(4) :
            if( 0<k+rdis[o]<=n and 0<l+cdis[o]<=n ) : 
                if mapp[k+rdis[o]][l+cdis[o]] in dict[mapp[k][l]] :
                    favorite+=1
        # 0, 1이면 1, 2이면 10, 3이면 100, 4이면 1000이다.
        if cmp_favorite==1 : total+=1
        elif cmp_favorite==2 : total+=10
        elif cmp_favorite==3 : total+=100
        elif cmp_favorite==4 : total+=1000

print(total)
