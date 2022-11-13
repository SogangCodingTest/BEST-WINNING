import enum
import sys
# 세로길이, 가로길이
# 세로길이가 최대 높이지 
h,w = map(int, sys.stdin.readline().split())
#  블록이 쌓인 높이, w개 주어진다
lis = list(map(int, sys.stdin.readline().strip().split()))

# 내 왼쪽 애 중 가장 큰 애, 오른쪽에서 가장 큰 애
water = 0


for i in range(1,len(lis)-1) : 
    maxleft, maxright = lis[i],lis[i]
    maxleft = max(lis[:i])
    maxright = max(lis[i+1:])
    standard = min(maxleft, maxright)
    if(standard > lis[i]) : #  그렇게 구한 애가 나보다 작을 때 ! 
        water+= (standard-lis[i])

print(water )

# 딴 사람 초간단 풀이 

# 파이썬 enumerate ? 
# for entry in enumerate(['A', 'B', 'C']):
# ...     print(entry)
# ...
# (0, 'A')
# (1, 'B')
# (2, 'C')

# h,w=map(int,input().split())
# m=list(map(int,input().split()))
# s=0
# for i,d in enumerate(m):
#     # 자기를 포함시켜놓네
#     s+=min(max(m[:i+1]),max(m[i:]))-d

# print(s)
# 출처: https://e-you.tistory.com/228 [Development:티스토리]
