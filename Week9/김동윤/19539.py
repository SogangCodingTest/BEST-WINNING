import sys

n = int(sys.stdin.readline().strip())
# 이하가 뒷뜰에 심은 사과나무의 개수
impossible = True; cnt=0
treelis = list(map(int, (sys.stdin.readline().strip()).split()))
# 갊자가 바라는 i번째 나무의 높이

# 하루에 길이를 총 3 늘이는 것 => 높이의 총 합은 3의 배수(3으로 나눠떨어지기)

if sum(treelis)%3==0 : 
    for i in range(n) : 
        # 1, 2 모두 사용하여 만들어
        cnt+= treelis[i]//2  # 나무에서 2를 사용한 횟수
    
    if cnt >= sum(treelis)//3 : 
        impossible=False
        
if impossible : print("NO")
else : print("YES")
