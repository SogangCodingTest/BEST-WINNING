import sys

#  최대 K만큼의 무게만을 넣을 수 있는 배낭만

n,k = map(int, sys.stdin.readline().rstrip().split()) 
# N : 첫 줄에 물품의 수 
# K : 준서가 버틸 수 있는 무게 

wvsave = []
# W, V : 무게, 즐거움
for i in range(n) : 
    w,v = map(int, sys.stdin.readline().rstrip().split()) 
    wvsave.append((w,v))

bag = [0 for _ in range(k+1)]

for b in range(n) :
    w,v = wvsave[b]
    for m in range(k, w-1, -1) : 
        # 처음에는 인덱스 0 부터 끝까지로 했는데, 이러면 누적됨
        # (ex) 아래같이 input 들어오고 0->3 검사하면
        #  (0, 5, 10, 15) 일케 쌓임 
        # 3 5
        # 4 2
        # 3 4
        # 1 5
        # 따라서 3->0 으로 검사하면 (0, 5, 5, 5) 로 쌓임
        # 만약 물건이 지금처럼 하나 아니고 누적인 경우엔 0부터,
        # 이렇게 하나인 경우에는 뒤에서부터 검사! 
        bag[m] = max(bag[m], bag[m-w]+v)

print(bag[-1])

