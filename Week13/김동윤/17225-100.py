import sys
# 구현
# 자료 구조
# 우선순위 큐
# 큐
a,b,n = map(int, sys.stdin.readline().split())
order = []
for i in range(n ) : 
    t,c,m = sys.stdin.readline().split()
    for mm in range(int(m)) : 
        if c  == 'B' : 
            order.append((int(t)+mm*a,c))
        else : 
            order.append((int(t)+mm*a,c))


order.sort() # 손님 주문 시간 순 정렬 

slis = []
jlis = []

for o in range(len(order)) : 
    if order[o][1]  == 'B' : 
        slis.append(str(o+1))
    else : 
        jlis.append(str(o+1))

print(len(slis))
print(" ".join(slis))
print(len(jlis))
print(" ".join(jlis))
