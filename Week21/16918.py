import sys

# 네 방향 탐색용
rdis = [-1, 1, 0, 0]
cdis = [0, 0, 1, -1]

def solution(r,c,n,mapp) : 
    
    while n<=time : # 시간이 아직 안됐을 경우에

        if n%2== 0 : # 폭탄 없는 곳에도 폭탄 설치해주기 
            # 2초마다 한번씩 하는 것, 
            # 2초, 4초, 6초 마다 작업 
            # 수행해주니깐 짝수일 때만 아래 작업 수행
            for i in range(r) :
                for j in range(c) :
                    if type(mapp[i][j])==str and mapp[i][j]=="." :
                        mapp[i][j] = 3

        for i in range(r) :
            for j in range(c) :
                if type(mapp[i][j])==int :
                    if mapp[i][j]==0 :  # 폭탄이 터질 타임
                        for k in range(4) :
                            if 0<=i+rdis[k]<r and 0<=j+cdis[k]<c and type(mapp[i+rdis[k]][j+cdis[k]]) == int and mapp[i+rdis[k]][j+cdis[k]]!=0 :
                                mapp[i+rdis[k]][j+cdis[k]] = "."
                        mapp[i][j]="." # 나 자신도 터져주기 
        
        # 나머지 폭탄들 시간 줄여주기 
        for i in range(r) :
            for j in range(c) :
                if type(mapp[i][j])==int :
                    if mapp[i][j]>0 :
                        mapp[i][j]-=1

        n+=1
### main
r,c,time = map(int, sys.stdin.readline().split())
mapp = []
for i in range(r) :
        mapp.append(list(sys.stdin.readline().rstrip()))

for i in range(r) :
    for j in range(c) :
        if mapp[i][j]=="O" :
            mapp[i][j]=2

solution(r,c,1,mapp) # 1초 동안 암것도 안해서 1초부터 넣어줌

for m in mapp:
    for mm in m :
        if type(mm)==int : 
            print("O", end= "")
        else : print(mm, end= "")
    print()    
    