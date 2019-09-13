line = [int(ch) for ch in input().split(' ')]
N, M, S, D = line[0], line[1], line[2], line[3]
cakes = [int(ch) for ch in input().split(' ')]
matrix = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(N):
    line = [int(ch) for ch in input().split(' ')]
    matrix[line[0]][line[1]] = line[2]


no_direct_graph = []

for i in range(M):
    line = [int(ch) for ch in input().split(' ')]
    no_direct_graph.append(line[0], line[1])

start_end = list(map(int, input().split()))

dict_graph = {}

for k in range(len(no_direct_graph)):  # 对于无向图中的每一条边
    for j in range(N):
        if no_direct_graph[k][0] == j + 1:
            if j + 1 not in dict_graph:
                dict_graph[j + 1] = [no_direct_graph[k]]
            else:
                dict_graph[j + 1].append(no_direct_graph[k])
        elif no_direct_graph[k][1] == j + 1:
            if j + 1 not in dict_graph:
                dict_graph[j + 1] = [
                    [no_direct_graph[k][1], no_direct_graph[k][0], no_direct_graph[k][2], no_direct_graph[k][3]]]
            else:
                dict_graph[j + 1].append(
                    [no_direct_graph[k][1], no_direct_graph[k][0], no_direct_graph[k][2], no_direct_graph[k][3]])
# print(dict_graph)   以字典的形式构造无向图

visited = []
unvisited = [_ + 1 for _ in range(N)]

distance = [float('inf') for _ in range(N)]

money = [0 for _ in range(N)]

temp = start_end[0]
# money[temp - 1] = 0
distance[temp - 1] = 0
for j in range(N):
    temp_neighbor = dict_graph[temp]
    for route in temp_neighbor:
        # print('route',route)
        if route[1] not in visited:  # 如果当前节点的邻居节点没有被访问过
            if distance[temp - 1] + route[2] < distance[route[1] - 1]:
                distance[route[1] - 1] = distance[temp - 1] + route[2]
                # print(route[-1])
                money[route[1] - 1] = money[temp - 1] + route[-1]
            elif distance[temp - 1] + route[2] == distance[route[1] - 1]:  # 如果距离相等，取花费少的路径
                if money[temp - 1] + route[-1] < money[route[1] - 1]:
                    distance[route[1] - 1] = distance[temp - 1] + route[2]
                    money[route[1] - 1] = money[temp - 1] + route[-1]
    # 找到money数组中除了当前temp的money值之外剩下的所有元素中最小money数量的位置，作为下一个temp位置
    distance_compare = distance.copy()
    distance_compare[temp - 1] = float("inf")

    visited.append(temp)
    if temp in unvisited:
        unvisited.remove(temp)

    min_value = float("inf")
    min_index = 0

    for k in range(N):
        if k + 1 in unvisited:  # 如果当前的节点并没有被访问过
            if distance_compare[k] < min_value:
                min_value = distance_compare[k]
                min_index = k
    temp = min_index + 1

print(distance[start_end[-1] - 1], money[start_end[-1] - 1])
