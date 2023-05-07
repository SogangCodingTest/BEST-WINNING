# 백준 14500번: 테트로미노 (2회차)

import sys

input = sys.stdin.readline

# 4 <= N, M <= 5 * 10^2
N, M = map(int, input().rstrip().split())

board = [list(map(int, input().rstrip().split())) for _ in range(N)]

# 5개의 테트로미노를 회전, 대칭시킨 모든 모양의 경우의 수 -> 19개
# 각 모양마다 탐색할 수 있는 최대 칸 수: 6개
# 각 모양마다 넣을 수 있는 최대 시작점: 5 * 10^2
# -> 브루트포싱

tetrominos = (
    # ####
    ((1, 4), (0, 0), (0, 1), (0, 2), (0, 3)),

    # #
    # #
    # #
    # #
    ((4, 1), (0, 0), (1, 0), (2, 0), (3, 0)),

    # ##
    # ##
    ((2, 2), (0, 0), (0, 1), (1, 0), (1, 1)),

    # #
    # #
    # ##
    ((3, 2), (0, 0), (1, 0), (2, 0), (2, 1)),

    #  #
    #  #
    # ##
    ((3, 2), (0, 1), (1, 1), (2, 0), (2, 1)),

    # ###
    # #
    ((2, 3), (0, 0), (0, 1), (0, 2), (1, 0)),

    # ###
    #   #
    ((2, 3), (0, 0), (0, 1), (0, 2), (1, 2)),

    # ##
    # #
    # #
    ((3, 2), (0, 0), (0, 1), (1, 0), (2, 0)),

    # ##
    #  #
    #  #
    ((3, 2), (0, 0), (0, 1), (1, 1), (2, 1)),

    # #
    # ###
    ((2, 3), (0, 0), (1, 0), (1, 1), (1, 2)),

    #   #
    # ###
    ((2, 3), (0, 2), (1, 0), (1, 1), (1, 2)),

    # #
    # ##
    #  #
    ((3, 2), (0, 0), (1, 0), (1, 1), (2, 1)),

    #  #
    # ##
    # #
    ((3, 2), (0, 1), (1, 0), (1, 1), (2, 0)),

    #  ##
    # ##
    ((2, 3), (0, 1), (0, 2), (1, 0), (1, 1)),

    # ##
    #  ##
    ((2, 3), (0, 0), (0, 1), (1, 1), (1, 2)),

    #  #
    # ###
    ((2, 3), (0, 1), (1, 0), (1, 1), (1, 2)),

    # ###
    #  #
    ((2, 3), (0, 0), (0, 1), (0, 2), (1, 1)),

    # #
    # ##
    # #
    ((3, 2), (0, 0), (1, 0), (1, 1), (2, 0)),

    #  #
    # ##
    #  #
    ((3, 2), (0, 1), (1, 0), (1, 1), (2, 1))
)

max_sum = 0

for size, *offsets in tetrominos:
    n, m = size

    for r in range(N - n + 1):
        for c in range(M - m + 1):
            current_sum = 0

            for dr, dc in offsets:
                current_sum += board[r + dr][c + dc]

            max_sum = max(max_sum, current_sum)
    
print(max_sum)
