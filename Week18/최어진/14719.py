# 14719번 : 빗물

# sys.stdin.readline() 사용
import sys

H, W = map(int, sys.stdin.readline().rstrip().split())
maps = [[0 for _ in range(W)] for _ in range(H)]
blocks = list(map(int, sys.stdin.readline().rstrip().split()))
for w in range(W):
    for block in range(blocks[w]):
        maps[block][w] = 1

for lines in maps:
    for line in lines:
        print(line, end = ' ' )
    print()
