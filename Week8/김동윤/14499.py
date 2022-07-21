import sys

n,m, x,y, k = map(int, sys.stdin.readline().split())

# 1) 지도 기록
mapp =[]
for i in range(n) :
    mapp.append(list(map(int, sys.stdin.readline().split())))

# 2) 이동 방향 기록
loc = map(int, sys.stdin.readline().split())
dice = [0 for _ in range(6)]

# 4) 각 대응하는 밑-윗
pair = {0:5, 1:4, 2:3, 3:2, 4:1, 5:0} 

for l in loc : 

    if l==1: # 동 
        tmpx = x; tmpy=y+1

    elif l==2 : # 서
        tmpx = x; tmpy=y-1
        
    elif l==3 : # 북 
        tmpx = x-1; tmpy=y

    else : # 남 
        tmpx = x+1; tmpy=y

    if 0>tmpx or tmpx>=n  or 0>tmpy or tmpy>=m: 
        # 영역 벗어나면 걍 옮기지도 않고 다시 for 문으로 돌아가 
        continue

    else : 
        x=tmpx; y=tmpy
        if l==1: # 동 
            dice[0], dice[2],dice[3], dice[5] = dice[2], dice[5],dice[0], dice[3]
        elif l==2 : # 서
            dice[0], dice[2],dice[3], dice[5] = dice[3], dice[0],dice[5], dice[2]

        elif l==3 : # 북 
            dice[0], dice[1],dice[4], dice[5] = dice[1], dice[5],dice[0], dice[4]

        else : # 남 
            dice[0], dice[1],dice[4], dice[5] = dice[4], dice[0],dice[5], dice[1]
        
        if mapp[x][y]!=0 : 
            # 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사 & 칸에 쓰여 있는 수는 0
            dice[5] = mapp[x][y]
            mapp[x][y] = 0

        else : 
            # 주사위의 바닥면에 쓰여 있는 수가 칸에 복사
            mapp[x][y] = dice[5]

    print(dice[0])
