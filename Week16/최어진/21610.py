# 백준 21610번 : 마법사 상어와 비바라기 (구현)
# 문제 읽고 이해하는 데 : 5분

import sys
import pprint

N, M = map(int, sys.stdin.readline().rstrip().split())
board = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
moves = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(M)]
cloud = [[N - 2, 0], [N - 2, 1], [N - 1, 0], [N - 1, 1]]
direction = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]

pprint.pprint(board)
print('=================')

for dir_idx, move in moves:
    print(dir_idx, move)

    # 1. 모든 구름이 di 방향으로 si칸 이동한다.
    cloud_r_move, cloud_c_move = direction[dir_idx][0] * move, direction[dir_idx][1] * move

    for i in range(len(cloud)):
        cloud[i][0], cloud[i][1] = cloud[i][0] + cloud_r_move, cloud[i][1] + cloud_c_move



    pprint.pprint(board)
    print()