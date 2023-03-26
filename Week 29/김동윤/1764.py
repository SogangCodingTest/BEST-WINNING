from collections import defaultdict
import sys

N,M = map(int,sys.stdin.readline().rstrip().split())
db = defaultdict() 
answer = []
# 듣도 못한 사람의 이름
for i in range(N) : 
    db[str(sys.stdin.readline().rstrip())] = 1 
# 보도 못한 사람의 이름
for i in range(M) : 
    name = str(sys.stdin.readline().rstrip())
    if name in db.keys() :
        answer.append(name)

answer.sort()
print(len(answer))
print("\n".join(answer))
