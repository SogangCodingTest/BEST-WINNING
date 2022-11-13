from cmath import sqrt
import sys

r,c = map(int, sys.stdin.readline().split())
store_cnt = int(sys.stdin.readline())
store = []

for i in range(store_cnt):
    sloc, sdis = map(int, sys.stdin.readline().split())
    store.append((sloc, sdis))

def distance(loc , dist ) :
    if loc==1 :
        return dist

    elif loc ==2 :
        return (r-dist)+c+r

    elif loc == 3 :
        return 2*r+c+(c-dist)

    else : 
        return r+dist

dloc, dis = map(int, sys.stdin.readline().split())
res = 0

d_dis = distance(dloc, dis)

for i in range(store_cnt) :
    now_srow, now_scol = store[i]
    s_dis = distance(now_srow, now_scol)
    cand1 = abs(d_dis-s_dis)
    cand2 = 2*r+2*c-cand1
    res+= min(cand1, cand2)

print(res)
