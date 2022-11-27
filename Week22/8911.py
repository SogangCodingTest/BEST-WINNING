import sys
# F: 한 눈금 앞으로 /  B: 한 눈금 뒤로
# L: 왼쪽으로 90도 회전 / R: 오른쪽으로 90도 회전



dir = [
    # F(0)         B(1)
    [ [0, 1 ] ,  [0, -1] ], # 북 
    [ [1, 0 ] ,  [-1, 0] ], # 동
    [ [0, -1] ,  [ 0, 1] ], # 남
    [ [-1, 0] ,  [1,  0] ], # 서
]

t = int(sys.stdin.readline())

case = []
road = []
for i in range(t) : 
    case.append(list(sys.stdin.readline().strip()))

for i in range(t) :
    # 초기화 작업 - 북 (왼 ) 동 남 서 position
    pos = 0 
    # 현재 좌표 (r,c)
    disr = 0 
    disc = 0
    road=[(0,0)]
    
    for v in range(len(case[i])) : 
        if case[i][v] == 'F' :  
            disr+=dir[pos][0][0]
            disc+=dir[pos][0][1]
        elif case[i][v] == 'B' : 
            disr+=dir[pos][1][0]
            disc+=dir[pos][1][1]
        elif case[i][v] == 'L' : 
            pos-=1
            if(pos<0) : 
                pos+=4
            pos%=4 # 0 1 2 3 중에서 하나이므로
        elif case[i][v] == 'R' : 
            pos+=1
            pos%=4 # 0 1 2 3 중에서 하나이므로
        road.append((disr, disc))

    # ((가장 큰 x좌표)-(가장 작은 x좌표))*((가장 큰 y좌표)-(가장 작은 y좌표))가 넓이다.
    width = max(road, key = lambda x:x[0])[0] - min(road, key = lambda x:x[0])[0]
    height = max(road, key = lambda x:x[1])[1] - min(road, key = lambda x:x[1])[1]
    print(width * height)
