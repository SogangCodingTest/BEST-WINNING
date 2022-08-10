########## 숏코딩 1회차 ##########
# import sys
# maps = [[False] * 100 for _ in range(100)]
# N = int(sys.stdin.readline().rstrip())


########## 숏코딩 2회차 ##########
# for _ in range(N):
#     x, y = map(int, sys.stdin.readline().rstrip().split())

#     for i in range(y, y + 10):
#         for j in range(x, x + 10):
#             maps[i][j] = True
# cnt = 0
# for line in maps:
#     cnt += line.count(True)
# print(cnt)


########## 숏코딩 3회차 ##########
# N = int(input())
# papers = [list(map(int, input().split())) for _ in range(N)]
# cnt = 0
# for i in range(100):
#     for j in range(100):
#         flag = True
#         for x, y in papers:
#             if x <= i and i < x + 10 and y <= j and j < y + 10:
#                 cnt += 1
#                 break
# print(cnt)


########## 숏코딩 4회차 ##########
# N = int(input())
# papers = [list(map(int, input().split())) for _ in range(N)]
# dots = []
# for i in range(100):
#     for j in range(100):
#         li = [(x, y) for x, y in papers if x <= i and i < x + 10 and y <= j and j < y + 10]
#         if len(li) != 0: dots.append(0)
# print(len(dots))


########## 숏코딩 5회차 ##########
# N = int(input())
# papers = [list(map(int, input().split())) for _ in range(N)]
# cnt = 0
# for i in range(100):
#     for j in range(100):
#         cnt += 1 if len([(x, y) for x, y in papers if x <= i and i < x + 10 and y <= j and j < y + 10]) != 0 else 0
# print(cnt)


########## 숏코딩 6회차 ##########
# N = int(input())
# papers = [list(map(int, input().split())) for _ in range(N)]
# answer = []
# for i in range(100):
#     for j in range(100):
#         answer.append(1 if len([(x, y) for x, y in papers if x <= i and i < x + 10 and y <= j and j < y + 10]) != 0 else 0)
# print(answer.count(1))


########## 숏코딩 7회차 ##########
N = int(input())
papers = [list(map(int, input().split())) for _ in range(N)]
print(len([1 for j in range(100) for i in range(100) if len([(x, y) for x, y in papers if x <= i and i < x + 10 and y <= j and j < y + 10]) != 0]))