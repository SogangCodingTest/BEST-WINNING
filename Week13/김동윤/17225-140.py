# 다수의 손님이 같은 색상으로 포장을 하는데 손님이 주문한 시간에 앞에 손님의 포장이 
# 끝나지 않았을 경우를 생각해서 
# 손님이 주문한 시간에 앞의 
# 손님의 포장이 끝나지 않았다면 그 시간만큼 딜레이
import sys
# 구현
# 자료 구조
# 우선순위 큐
# 큐
a,b,n = map(int, sys.stdin.readline().split()) 
# a가 블루인 상미니 시간 b가 레드인 지미니 시간 

order = []
for i in range(n ) : 
    t,c,m = sys.stdin.readline().split()
    for mm in range(int(m)) : 
        if c  == 'B' : 
            order.append((int(t)+mm*a,c))
        else : 
            order.append((int(t)+mm*a,c))

# 다수의 손님이 같은 색상으로 포장을 하는데 
# 손님이 주문한 시간에 앞에 손님의 포장이 끝나지 않았을 
# 경우를 생각해서 손님이 주문한 시간에 
# 앞의 손님의 포장이 끝나지 않았다면 
# 그 시간만큼 딜레이

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
