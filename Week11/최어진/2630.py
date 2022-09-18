# sys.stdin.readline 사용
import sys
# log2() 사용
import math

# 초기 전체 정사각형 색종이의 한 변의 길이 N 입력
N = int(sys.stdin.readline().rstrip())
# 색종이 각 칸의 정보 입력
papers = [tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

# 흰 색과 파란 색 각각의 색종이 갯수 초기화
white = 0
blue = 0

# 가장 큰 색종이를 몇 번 분할해야 하는지의 여부 N 계산
N = int(math.log2(N))

# 분할 탐색을 위한 solve() 함수 정의
def solve(N, r_begin, r_end, c_begin, c_end):
    # 경우 1 : 색종이의 모든 칸의 색상이 하나로 같을 경우
    color = papers[r_begin][c_begin]

    flag = True
    for i in range(r_begin, r_end + 1):
        for j in range(c_begin, c_end + 1):
            if color != papers[i][j]:
                flag = False

    if flag:
        # --> 큰 하나의 정사각형으로 보고 색종이 갯수를 하나 누적함
        global white, blue
        if color == 1:
            blue += 1
        else:
            white += 1
        return

    # 경우 2 : 색종이의 모든 색상이 같지는 않지만,
    #       더 이상 쪼갤 수는 없는 크기인 경우
    if N == 1:
        for i in range(r_begin, r_end + 1):
            for j in range(c_begin, c_end + 1):
                # --> 색종이의 가장 작은 한 칸씩을 색종이 갯수로 취급해 갯수를 누적함
                if papers[i][j] == 1:
                    blue += 1
                else:
                    white += 1

    # 경우 3 : 색종이의 모든 색상이 같지 않으며,
    #       쪼갤 수 있는 크기인 경우 (N > 1)
    else:
        ###########
        #  1 | 2  #
        #----+----#
        #  3 | 4  #
        ###########

        # --> 큰 하나의 정사각형을 작은 정사각형 4개로 나누어 분할 탐색 수행 (재귀 함수 호출)

        # 1
        solve(N - 1, r_begin, (r_begin + r_end) // 2, c_begin, (c_begin + c_end) // 2)
        # 2
        solve(N - 1, r_begin, (r_begin + r_end) // 2, (c_begin + c_end) // 2 + 1, c_end)
        # 3
        solve(N - 1, (r_begin + r_end) // 2 + 1, r_end, c_begin, (c_begin + c_end) // 2)
        # 4
        solve(N - 1, (r_begin + r_end) // 2 + 1, r_end, (c_begin + c_end) // 2 + 1, c_end)

# 맨 처음 가장 큰 색종이에 대해 분할 탐색 수행
solve(N, 0, 2**N - 1, 0, 2**N - 1)

# 정답 출력
print(white)
print(blue)