import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())

# n: 변의 길이,x: 현재 위치의 x축 값, y:현재 위치의 y축 값
result = 0
def N(n, x, y):
    global result

    if x==r and y==c:
        print(int(result))
        exit(0)

    if n == 1:
        result += 1
        return

    if not(x<=r<x+n and y<=c<y+n):
        result += n*n
        return
# 1->2->3->4 분면 순으로 재귀를 돌고 넘어가면서
# result 를 하나씩 늘리면 그것이 순서닷 
    # 1사분면
    N(n/2, x, y) # 1사분면 싸아악 돌고 
    # 2사분면
    N(n/2, x, y+n/2) # 2사분면 싸아악 돌고 ... 
    # 3사분면
    N(n/2, x+n/2, y)
    # 4사분면
    N(n/2, x+n/2, y+n/2)

N(2**n, 0, 0)

# 4개씩 쪼개서 (r,c)가 있는 위치가 아니라면 나머지 3분면에 있는 갯수 
# 그리고 (r,c)가 존재하는 분면을 다시 4등분해서 똑같이 탐색 
# 총 4개의 정사각형만 남았을 때, 정사각형 한개씩 탐색을 해서 (r,c)가 아니라면 1만 더해주고 리턴 
# (r,c)가 있는 곳까지 왔을 때, 지금까지 더해준 result를 출력 
