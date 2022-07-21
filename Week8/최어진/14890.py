# sys.stdin.readline() 사용
import sys

# 정사각형 모양의 칸의 너비 N, 경사로의 가로 길이 L 입력
N, L = map(int, sys.stdin.readline().rstrip().split())

# 정사각형 모양의 칸들 높이 정보 입력
maps = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

# 존재하는 12개 경로 중 지나갈 수 있는 길의 개수를 카운트하는 변수 0으로 초기화
cnt = 0

# 열 방향의 N개 경로에 대해서 검사
for i in range(N):
    # 1. 첫번째 칸의 높이를 `current`에 저장하고
    current = maps[i][0]
    # flag를 `True`로 세팅
    flag = True
    # 각 칸에 하나의 경사로만 위치하도록 하기 위해 visited 리스트 선언
    visited = [False for _ in range(N)]

    # 2. 나머지 N-1개 칸에 대해 반복 -> `new_height` 
    for j in range(1, N):
        new_height = maps[i][j]

        # 2-1. 새로운 칸이 이전 칸과 같으면
        if new_height == current:
            # -> 넘어감
            pass

        # 2-2. 새로운 칸이 이전 칸보다 하나 높다면,
        elif new_height == current + 1:
            if j < L:
                flag = False
                break

            # 이전 칸부터 포함해서 왼쪽으로 L개의 칸 같은지 검사 후,
            l_flag = True
            for k in range(L):
                # 같지 않거나 이미 경사로가 놓아져 있다면 flag를 False로 세팅
                if current != maps[i][j - 1 - k] or visited[j - 1 - k]:
                    l_flag = False
                    break
            
            if not l_flag:
                flag = False
                break
            else:
                # 경사로를 놓을 수 있게 된 경우에는,
                for k in range(L):
                    # 해당하는 칸들에 대해 visited를 True로 세팅
                    visited[j - 1 - k] = True

        # 2-3. 새로운 칸이 이전 칸보다 하나 낮다면,
        elif new_height == current - 1:
            if j > N - L:
                flag = False
                break

            # 새로운 칸 포함 오른쪽으로 L개의 칸 같은지 검사 후,
            l_flag = True
            for k in range(L):
                # 같지 않거나 이미 경사로가 놓아져 있다면 flag를 False로 세팅
                if new_height != maps[i][j + k] or visited[j + k]:
                    l_flag = False
                    break

            if not l_flag:
                flag = False
                break
            else:
                # 경사로를 놓을 수 있게 된 경우에는,
                for k in range(L):
                    # 해당하는 칸들에 대해 visited를 True로 세팅
                    visited[j + k] = True

        # 2-4. 이외에는 칸의 높이가 2개 이상 차이나므로,
        else:
            # flag를 False로 세팅
            flag = False
            break

        # 다음 칸을 가리키기 전에 현재 칸을 이전 칸에 덮어씌우기
        current = new_height

    # 3. N-1개 칸을 전부 탐색한 결과 flag가 True라면,
    if flag:
        # 갈 수 있는 경로 1 누적
        cnt += 1

# 행 방향의 N개 경로에 대해서 검사
for j in range(N):
    # 1. 첫번째 칸의 높이를 `current`에 저장하고
    current = maps[0][j]
    # flag를 `True`로 세팅
    flag = True
    # 각 칸에 하나의 경사로만 위치하도록 하기 위해 visited 리스트 선언
    visited = [False for _ in range(N)]

    # 2. 나머지 N-1개 칸에 대해 반복 -> `new_height` 
    for i in range(1, N):
        new_height = maps[i][j]

        # 2-1. 새로운 칸이 이전 칸과 같으면
        if new_height == current:
            # -> 넘어감
            pass

        # 2-2. 새로운 칸이 이전 칸보다 하나 높다면,
        elif new_height == current + 1:
            if i < L:
                flag = False
                break

            # 이전 칸부터 포함해서 왼쪽으로 L개의 칸 같은지 검사 후,
            l_flag = True
            for k in range(L):
                # 같지 않거나 이미 경사로가 놓아져 있다면 flag를 False로 세팅
                if current != maps[i - 1 - k][j] or visited[i - 1 - k]:
                    l_flag = False
                    break
            
            if not l_flag:
                flag = False
                break
            else:
                # 경사로를 놓을 수 있게 된 경우에는,
                for k in range(L):
                    # 해당하는 칸들에 대해 visited를 True로 세팅
                    visited[i - 1 - k] = True

        # 2-3. 새로운 칸이 이전 칸보다 하나 낮다면,
        elif new_height == current - 1:
            if i > N - L:
                flag = False
                break

            # 새로운 칸 포함 오른쪽으로 L개의 칸 같은지 검사 후,
            l_flag = True
            for k in range(L):
                # 같지 않거나 이미 경사로가 놓아져 있다면 flag를 False로 세팅
                if new_height != maps[i + k][j] or visited[i + k]:
                    l_flag = False
                    break

            if not l_flag:
                flag = False
                break
            else:
                # 경사로를 놓을 수 있게 된 경우에는,
                for k in range(L):
                    # 해당하는 칸들에 대해 visited를 True로 세팅
                    visited[i + k] = True

        # 2-4. 이외에는 칸의 높이가 2개 이상 차이나므로,
        else:
            # flag를 False로 세팅
            flag = False
            break

        # 다음 칸을 가리키기 전에 현재 칸을 이전 칸에 덮어씌우기
        current = new_height

    # 3. N-1개 칸을 전부 탐색한 결과 flag가 True라면,
    if flag:
        # 갈 수 있는 경로 1 누적
        cnt += 1

# 정답 출력
print(cnt)