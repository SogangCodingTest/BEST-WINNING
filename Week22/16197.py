import sys

n, m = map(int, sys.stdin.readline().split())
map = []

for i in range(n) : 
    map.append(list(sys.stdin.readline().strip()))

# 첫째 줄에 두 동전 중 하나만 보드에서 떨어뜨리기 위해 
# 눌러야 하는 버튼의 최소 횟수를 출력한다. 

# 만약, 두 동전을 떨어뜨릴 수 없거나, 
# 버튼을 10번보다 많이 눌러야 한다면, -1을 출력

# 버튼은 "왼쪽", "오른쪽", "위", "아래"와 같이 4가지가 있다. 
# 버튼을 누르면 두 동전이 버튼에 쓰여 있는 방향으로 동시에 이동 

# 1) 동전이 이동하려는 칸이 벽이면, 동전은 이동하지 않는다.
# 2) 동전이 이동하려는 방향에 칸이 없으면 동전은 보드 바깥으로 떨어진다.
# 3) 그 외의 경우에는 이동하려는 방향으로 한 칸 이동한다.
# 이동하려는 칸에 동전이 있는 경우에도 한 칸 이동한다.
