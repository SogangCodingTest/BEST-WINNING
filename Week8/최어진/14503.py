# sys.stdin.readline() 사용
import sys

# 방의 세로 크기 N, 가로 크기 M 입력
N, M = map(int, sys.stdin.readline().rstrip().split())

# 로봇 청소기의 세로 좌표 r, 가로 좌표 c, 초기 방향 d 입력
r, c, d = map(int, sys.stdin.readline().rstrip().split())

# 방의 비어있는 칸과 막혀 있는 칸에 대한 정보 입력
maps = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
# 방의 각 칸의 청소(방문) 여부를 기록하기 위한 cleaned 리스트 선언
cleaned = [[False for _ in range(M)] for _ in range(N)]

# 바라보는 방향에 따른 좌표 계산 쉽게 하기 위한 방향 설정
front = [[-1, 0], [0, 1], [1, 0], [0, -1]]
back = [[1, 0], [0, -1], [-1, 0], [0, 1]]
left = [[0, -1], [-1, 0], [0, 1], [1, 0]]

# 로봇 청소기가 바라보는 초기 방향 -> offset 변수
offset = d

# 로봇 청소기의 작동 과정
flag = True
while True:
    ########## 디버깅 용도로 보기 편하게 작성 ##########
    # for i in range(N):
    #     for j in range(M):
    #         if i == r and j == c:
    #             if offset == 0:
    #                 print('^', end=' ')
    #             elif offset == 1:
    #                 print('>', end=' ')
    #             elif offset == 2:
    #                 print('v', end=' ')
    #             elif offset == 3:
    #                 print('<', end=' ')

    #         elif maps[i][j] == 1:
    #             print('#', end=' ')
    #         elif cleaned[i][j]:
    #             print('X', end = ' ')
    #         else:
    #             print(' ', end = ' ')
    #     print()
    # print()
    # input()
    #############################################

    # 1. 현재 위치를 청소한다.
    if flag:
        cleaned[r][c] = True

    # 2. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 탐색을 진행한다.
    flag = False
    for _ in range(4):
        # 2-1. 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면,
        if cleaned[r + left[offset][0]][c + left[offset][1]] == False and \
            maps[r + left[offset][0]][c + left[offset][1]] != 1:
            # 그 방향으로 회전한 다음
            offset = (offset + 3) % 4
            # 한 칸을 전진하고 1번부터 진행한다.
            r, c = r + front[offset][0], c + front[offset][1]
            flag = True
            break
        # 2-2. 왼쪽 방향에 청소할 공간이 없다면,
        else:
            # 그 방향으로 회전하고 2번으로 돌아간다.
            offset = (offset + 4 - 1) % 4

    # 이번에 도달한 칸이 청소할 수 있는 칸이면 flag가 True
    if flag:
        continue

    # 2-3. 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는,
    if maps[r + back[offset][0]][c + back[offset][1]] != 1:
        # 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
        r, c = r + back[offset][0], c + back[offset][1]
        continue
    # 2-4. 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는
    else:
        # 작동을 멈춘다.
        break

# 방 안의 모든 칸에 대해 청소한 칸의 개수를 검사
cnt = 0
for i in range(N):
    cnt += cleaned[i].count(True)

# 정답 출력
print(cnt)