import sys
n, r, c = map(int,sys.stdin.readline().strip().split())

seq = []
seq = [list(-1 for _ in range(2**n)) for _ in range(2**n)]

def recur ( r, c, width , parent) :
    if width > 2 :
        recur(r,    c,      width//2, 4*parent + 0)
        recur(r,    c+width//2,     width//2, 4*parent + 1)
        recur(r+width//2,   c,      width//2, 4*parent + 2)
        recur(r+width//2,   c+width//2,     width//2,   4*parent + 3)

    elif width==2 and 0<=r<2**n and 0<=c<2**n : # width가 2가 되는 순간에는 이제 seq 에 기록
        #print(r,c)
        seq[r][c] = 4*parent + 0
        seq[r][c+1] = 4*parent + 1
        seq[r+1][c] = 4*parent + 2
        seq[r+1][c+1] = 4*parent + 3

recur(0,0,2**n*2**n,0)

print(seq[r][c])

import sys
n, r, c = map(int,sys.stdin.readline().strip().split())

seq = []
seq = [list(-1 for _ in range(2**n)) for _ in range(2**n)]

def recur ( r, c, width , parent) :
    if width > 2 :
        recur(r,    c,      width//2, 4*parent + 0)
        recur(r,    c+width//2,     width//2, 4*parent + 1)
        recur(r+width//2,   c,      width//2, 4*parent + 2)
        recur(r+width//2,   c+width//2,     width//2,   4*parent + 3)

    elif width==2 and 0<=r<2**n and 0<=c<2**n : # width가 2가 되는 순간에는 이제 seq 에 기록
        #print(r,c)
        seq[r][c] = 4*parent + 0
        seq[r][c+1] = 4*parent + 1
        seq[r+1][c] = 4*parent + 2
        seq[r+1][c+1] = 4*parent + 3

recur(0,0,2**n*2**n,0)

print(seq[r][c])
