import sys
sys.setrecursionlimit(10 ** 6)

N = int(sys.stdin.readline())

image = [list(sys.stdin.readline().rstrip()) for _ in range(N)]


def dnc(r_start, r_end, c_start, c_end):
    # 모든 픽셀이 1인지 혹은 0인지 검사
    prev = image[r_start][c_start]
    flag = True

    for i in range(r_start, r_end + 1):
        for j in range(c_start, c_end + 1):
            if image[i][j] != prev:
                flag = False
 
            if not flag:
                break
        if not flag:
            break

    if flag:
        return prev 
    elif r_end - r_start == 1:
        return f"({image[r_start][c_start]}{image[r_start][c_end]}{image[r_end][c_start]}{image[r_end][c_end]})"
    else:
        return f"({dnc(r_start, r_start + ((r_end - r_start) // 2), c_start, c_start + ((c_end - c_start) // 2))}{dnc(r_start, r_start + ((r_end - r_start) // 2), c_start + ((c_end - c_start) // 2) + 1, c_end)}{dnc(r_start + ((r_end - r_start) // 2) + 1, r_end, c_start, c_start + ((c_end - c_start) // 2))}{dnc(r_start + ((r_end - r_start) // 2) + 1, r_end, c_start + ((c_end - c_start) // 2) + 1, c_end)})"


result = dnc(0, N - 1, 0, N - 1)
print(result)
