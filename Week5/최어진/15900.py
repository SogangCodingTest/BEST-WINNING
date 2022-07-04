# 트리의 노드 갯수 N 입력
N = int(input())

# 트리의 간선 리스트 초기화
links = {}

# 간선 정보 입력
for _ in range(N - 1):
    node, link = list(map(int, input().split()))
    if node - 1 in links.keys():
        links[node - 1].append(link - 1)
    elif link - 1 in links.keys():
        links[link - 1].append(node - 1)
    else:
        if link == 1:
            links[link - 1] = [node - 1]
        else:
            links[node - 1] = [link - 1]

total_link_sum = 0

def dfs(current_node, link_sum):
    global total_link_sum

    if current_node not in links.keys():
        total_link_sum += link_sum
        return
    
    for link in links[current_node]:
        dfs(link, link_sum + 1)

dfs(0, 0)

answer = "Yes" if total_link_sum % 2 == 1 else "No"
print(answer)