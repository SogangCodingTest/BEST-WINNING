import sys

n = int(sys.stdin.readline())

# n개를 
def recur(n, current_place, detour, target_place) : 
    if n==0:
        return
    recur(n-1, current_place, target_place, detour)    
    print(current_place, target_place)
    recur(n-1, detour, current_place, target_place)  

print(2**n-1)
# N이 1일 때 횟수 1
# N이 2일 때 횟수 3
# N이 3일 때 횟수 7
# N이 4일 때 횟수 15
# N이 5일 때 횟수 31

if n<=20 :
    recur(n, 1, 2, 3) # 1번에 있는 애들을 3번으로 이동시키겠다. 
