# sys.stdin.readline 사용
import sys
# 우선순위 큐 사용
import heapq

# 거인의 수 N, 센티의 키 H, 뿅망치 찬스 T 입력
N, H, T = map(int, sys.stdin.readline().rstrip().split())

# 거인 N명의 키를 우선순위 큐에 삽입
# 이 때, 내림차순 정렬을 위해 마이너스를 붙여서 삽입한다.
giants = [-int(sys.stdin.readline()) for _ in range(N)]
heapq.heapify(giants)

# 뿅망치 사용 횟수 초기화
cnt = 0

# 뿅망치 찬스만큼 반복
for i in range(T):
    # 가장 큰 거인의 키가 1이거나 센치보다 작은 경우
    if -giants[0] == 1 or -giants[0] < H:
        # 뿅망치 그만 때리고 탈출
        break

    # 가장 큰 거인의 키를 뿅망치로 두드려서 다시 큐에 삽입
    giant = heapq.heappop(giants)
    heapq.heappush(giants, -(-giant // 2))
    # 뿅망치 사용 횟수 ++
    cnt += 1

# 가장 큰 거인의 키가 센치보다 작을 경우
if -giants[0] < H:
    # 'YES' 와 뿅망치 사용 횟수 출력
    print('YES')
    print(cnt)
# 가장 큰 거인의 키가 아직 센치보다 같거나 클 경우
else:
    # 'NO' 와 가장 큰 거인의 키 출력
    print('NO')
    print(-giants[0])

# 이 문제에서 복습할 heapq 메서드들
# 1. heapq.heapify
# 2. heapq.heappush
# 3. heapq.heappop
