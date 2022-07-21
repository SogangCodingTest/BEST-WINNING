import sys
mapp = list([0 for _ in range(100)] for _ in range(100))
n = int(sys.stdin.readline().strip())
res = 0

for i in range(n) : 
    g, s = map(int, sys.stdin.readline().split())
    for j in range(s-1, s+9) :
        for i in range(g-1,g+9) :
            mapp[j][i] = 1

for m in mapp : 
    for mm in m :
        if mm==1 : res+=1

print(res)
