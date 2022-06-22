from collections import deque
from itertools import combinations
import sys

r = [0, 0, -1 , 1]
c = [-1, 1, 0, 0]

n, m = map(int,sys.stdin.readline().rstrip().split())
# 크기가 N×N인 도시
# 첫째 줄에 폐업시키지 않을 치킨집을 최대 M개

map = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# 0은 빈 칸, 1은 집, 2는 치킨집

chkn =[]
for i in range(n) :
    for j in range(n) :
        if map[i][j]==2 :
            chkn.append((i,j))

comb = list(combinations(chkn, m))

# 5 2
# [((0, 1), (3, 0)), ((0, 1), (4, 0)),  치킨 하우스의 리스트 
# ((0, 1), (4, 1)), ((0, 1), (4, 4)), 
# ((3, 0), (4, 0)), ((3, 0), (4, 1)), 
# ((3, 0), (4, 4)), ((4, 0), (4, 1)), 
# ((4, 0), (4, 4)), ((4, 1), (4, 4))]

total_chck_list=[]
min_dis = 0
for j in range(len(comb)) : #각 경우의 수를 돌아주기 
    current_chk_dis = 0 # `현재 경우의 치킨 거리`
    chk_list = comb[j] #현재 골랐다고 가정하는 치킨 하우스의 리스트 

    for i in range(n) :
        for j in range(n)  :
            if map[i][j] == 1 : # 집이라면
                min_dis = 99999

                for k in chk_list :
                    cmp_dis = abs(i-k[0]) + abs(j-k[1])

                    if cmp_dis < min_dis :
                    
                        min_dis = cmp_dis

            # 한 집 검사 끝나면 치킨 거리를 `현재 경우의 치킨 거리` 에 더하기
                current_chk_dis+= min_dis
                #print("home", min_dis)
            


    # 한 경우의 수 끝나면 치킨 거리를 total 리스트에 더하기 
    total_chck_list.append(current_chk_dis)

# print(total_chck_list)
print(min(total_chck_list))
