from collections import Counter
import sys

n = int(sys.stdin.readline().strip())
students = list(map(int,sys.stdin.readline().strip().split()))
students.sort()
# print(students)
std_counter = Counter(students) # 111 22 1:3개 2ㅣ2개
# 리스트나 셋을 인자로 넘기면 각 항목을 키로 해서 개수
res = 0
for i in range(n) : 
    s,e=i+1,n-1 # 나이 후 ~ 끝 전 
    target = -students[i]
    # print(i,target)
    while s<e : 
        cmp = students[s] + students[e]
        if cmp < target : 
            s+=1 # 증가하여야 하므로 시작점 오른쪽으로 

        elif cmp == target : # 중복 수 걸러줘야 하지 
            if students[s]==students[e] : # 만약 양쪽 같으면 
                res+= e-s  #사이에 있는 것 (+)
                # -4 0 (2) 2 2 (2) 3 => 인덱스 2와 5, 5-2 = 3 -> s+=1 하면 1+
            else : 
                res+= std_counter[students[e]] #students[s] 
            s+=1 # e-=1

        else : 
            e-=1 # 감소하여야 하므로 끝점 왼쪽으로 

print(res)
