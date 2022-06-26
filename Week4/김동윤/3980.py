import sys

def dfs(scr, pos) : # 점수, 몇번째 포지션인지 

    if pos == 11 :
        total_lis.append(scr)

    else :
        for i in range(11) :
            if visited[i] ==0 and people[i][pos]!=0 :
                scr+=people[i][pos]
                visited[i] = 1
                dfs(scr, pos+1)
                visited[i] = 0
                scr-=people[i][pos]

c = int(sys.stdin.readline().rstrip()) #test case
# 능력치가 0인 포지션에 배치될 수 없다.



for t in range(c) : 
    pos = [[] for _ in range(11)]
    people =[]

    for i in range(11) :
        # i 번째 선수의 능력치
        people.append(list(map(int, sys.stdin.readline().rstrip().split())))

    total_lis=[]
    scr = 0
    visited = [0]*11

    dfs(0,0)
    print(max(total_lis))
