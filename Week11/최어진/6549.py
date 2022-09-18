import sys

# 이거 주석 다 작성하고 나서 백준에도 제출하세요

# 1. 가운데 위치를 구한다.
# 2. 가운데 위치를 기준으로 분할하여 왼쪽 구간의 넓이와 오른쪽 구간의 넓이를 구한다.
# 3. 왼쪽과 오른쪽 중 큰 넓이를 변수에 저장한다.
# 4. 변수에 저장된 넓이와 두 구간을 합친 구간([lo : hi])의 가장 큰 넓이를 구해 두 개 중 가장 큰 넓이를 반환한다.

def Area(start, end):
    if start == end:
        return hist[start]

    # 1. 가운데 위치를 구한다.
    mid = (start + end) // 2

    # 2. 가운데 위치를 기준으로 분할하여 왼쪽 구간의 넓이와 오른쪽 구간의 넓이를 구한다.
    left_area = Area(start, mid)
    right_area = Area(mid + 1, end)

    # 3. 왼쪽과 오른쪽 중 큰 넓이를 변수에 저장한다.
    _max = left_area if left_area > right_area else right_area

    # 4. 변수에 저장된 넓이와 두 구간을 합친 구간([lo : hi])의 가장 큰 넓이를 구해 두 개 중 가장 큰 넓이를 반환한다.
    left, right = mid, mid
    height = hist[mid]

    while start < left and right < end:
        if hist[left - 1] > hist[right + 1]:
            height = hist[left - 1] if hist[left - 1] < height else height
            left -= 1
        else:
            height = hist[right + 1] if hist[right + 1] < height else height
            right += 1

        _max = height * (right + 1 - left) if height * (right + 1 - left) > _max else _max

    while start < left:
        height = hist[left - 1] if hist[left - 1] < height else height
        left -= 1
        _max = height * (right + 1 - left) if height * (right + 1 - left) > _max else _max

    while right < end:
        height = hist[right + 1] if hist[right + 1] < height else height
        right += 1
        _max = height * (right + 1 - left) if height * (right + 1 - left) > _max else _max

    return _max
    
answers = []

while True:
    line = sys.stdin.readline().rstrip().split()

    # 테스트 케이스 입력 종료 조건
    if line[0] == '0':
        break

    n, *hist = list(map(int, line))

    answers.append(Area(0, n - 1))

for answer in answers:
    print(answer)