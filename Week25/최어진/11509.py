import sys

input = sys.stdin.readline

N = int(input())

heights = list(map(int, input().rstrip().split()))
# print(heights)

answer = 0

while heights:
    arrow = max(heights)
    boom = 0
    
    for idx in range(len(heights)):
        if heights[idx - boom] == arrow:
            heights.pop(idx - boom)
            boom += 1
            arrow -= 1

    # print(heights)
    answer += 1

print(answer)

# 13분 2초 시간 초과
