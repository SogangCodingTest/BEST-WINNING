import sys

n = int(sys.stdin.readline())
lis = [0 for _ in range(n+1)]
lis[0] = 1 
lis[1] = 2
lis[2] = 7
special = 0

for i in range(3,n+1) : 
    special += lis[i-3]
    lis[i] = (2*lis[i-1] + 3*lis[i-2] + 2*special)%1000000007

print(lis[n] )
