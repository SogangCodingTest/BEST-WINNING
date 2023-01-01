import sys
import itertools
from collections import deque

n,k= map(int, sys.stdin.readline().split())
lis = list(map(int, sys.stdin.readline().split()))
cha = []
for i in range(1,n) :
    cha.append(lis[i]-lis[i-1])
cha.sort()
for j in range(k-1) :
    cha.pop()

print(sum(cha))
