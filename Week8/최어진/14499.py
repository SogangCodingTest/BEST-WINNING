# sys.stdin.readline() 사용
import sys

# 지도의 세로 크기 N, 가로 크기 M, 주사위의 세로 좌표 x, 가로 좌표 y, 명령의 개수 k 입력
N, M, x, y, k = map(int, sys.stdin.readline().rstrip().split())

# 지도의 정보를 2차원 리스트 형태로 입력
maps = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

# 주사위의 상태를 6개 방향에서 바라본 눈금을 저장하는 변수들 초기화
# (가장 처음에 주사위에는 모든 면에 0이 적혀져 있다.)
top = 0
bottom = 0
left = 0
right = 0
front = 0
back = 0

# k개 명령 입력 (동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4)
commands = list(map(int, sys.stdin.readline().rstrip().split()))

# 1. 주사위를 굴릴 방향(direction)을 입력받는다.
for direction in commands:
    # 2. 명령에 따라 (동쪽으로) 주사위를 굴릴 수 있다면,
    if direction == 1 and y < M - 1:
        # 해당 칸으로 주사위를 굴린다.
        y += 1
        left, top, right, bottom = bottom, left, top, right

    # 2. 명령에 따라 (서쪽으로) 주사위를 굴릴 수 있다면,
    elif direction == 2 and y > 0:
        # 해당 칸으로 주사위를 굴린다.
        y -= 1
        left, top, right, bottom = top, right, bottom, left
        
    # 2. 명령에 따라 (북쪽으로) 주사위를 굴릴 수 있다면,
    elif direction == 3 and x > 0:
        # 해당 칸으로 주사위를 굴린다.
        x -= 1
        front, top, back, bottom = bottom, front, top, back
        
    # 2. 명령에 따라 (남쪽으로) 주사위를 굴릴 수 있다면,
    elif direction == 4 and x < N - 1:
        # 해당 칸으로 주사위를 굴린다.
        x += 1
        front, top, back, bottom = top, back, bottom, front
        
    # 3. 잘못된 명령이라면 (지도를 벗어나거나 등의) 무시한다.
    else:
        continue

    # 2-1. 주사위가 놓인 지도의 칸이 0이라면,
    if maps[x][y] == 0:
        # 주사위의 아랫 면의 눈금을 지도의 칸에 복사한다. 
        maps[x][y] = bottom
    # 2-2. 주사위가 놓인 지도의 칸이 0이 아니라면,
    else:
        # 지도의 칸에 적힌 값을 주사위의 아랫면으로 덮어 씌우고
        bottom = maps[x][y]
        # 지도의 칸은 0으로 만든다.  
        maps[x][y] = 0

    # 2-3. 주사위의 윗 면 눈금을 출력한다.
    print(top)
