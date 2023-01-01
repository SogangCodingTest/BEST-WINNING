import sys
from collections import defaultdict

n = int(sys.stdin.readline().rstrip())
in_dict = defaultdict()
in_set = []

out = []
out_dict = defaultdict()
out_set = []

answer = 0

for j in range(n) :
    key = sys.stdin.readline().rstrip()
    in_dict[key] = in_set.copy() # 내 앞에 있던 애들 
    in_set.append(key) 

for j in range(n) :
    key = sys.stdin.readline().rstrip()
    out.append(key)
    out_dict[key] = out_set.copy()
    out_set.append(key)

for j in range(n) :
    if( len(set(in_dict[out[j]]) - set(out_dict[out[j]])) )>0:
        answer+=1
print(answer)
