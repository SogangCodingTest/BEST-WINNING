from math import sqrt
import sys

x, y, c = map(float,sys.stdin.readline().strip().split())
s,e = 0,min(x,y) # 각 밑변 범위는 빗변보다 클 수 없지 
answr = 0
while e-s>0.000001 : 
    width = (e+s)/2
    # 두 너비의 차이가 0.000001 이상일 경우에만 (s<e 내재)
    h1 = (x**2-width**2)**(1/2)
    h2 = (y**2-width**2)**(1/2)
    cmp = (h1*h2/(h1+h2))

    if cmp < c : 
        # c 보다 작으면 (c가 낮아질 수록) 너비는 커짐 
        e = width # 좁혀주자

    elif cmp >= c : 
        # c 보다 크면 (c가 높아질 수록) 너비는 좁아져
        answr = width # 너비 더 키워야 해 
        s = width

print(answr)

# 아이디어 + 참고 : https://githubseob.tistory.com/49

