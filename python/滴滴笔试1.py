import collections
line = [int(ch) for ch in input().split(' ')]
n, m, d = line[0], line[1], line[2]
s_idx = [int(ch) for ch in input().split(' ')]
parents = [int(ch) for ch in input().split(' ')]

node_map = collections.defaultdict(set)

for i in range(2, n+1):
    node_map[i].add(parents[i-2])
    node_map[parents[i-2]].add(i)

def find_nodes(node_map, d, root):
    res = []
    path = []
    helper(node_map, d, root, path, res)
    res_set = set()
    res_set.add(root)
    for p in res:
        res_set.add(p[-1])
    return res_set

def helper(node_map, d, root, path, res):
    if len(path) > d: return
    if len(path) > 0:
        res.append(path)
    for node in node_map[root]:
        if node not in path:
            helper(node_map, d, node, path+[node], res)

res_set = None
for root in s_idx:
    t_set = find_nodes(node_map, d, root)
    print(t_set)
    if res_set == None: res_set = t_set
    else: res_set = res_set & t_set

print(len(res_set))

