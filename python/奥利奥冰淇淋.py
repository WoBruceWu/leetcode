from functools import cmp_to_key
class IceCream(object):
    def __init__(self, w, v):
        self.w = w
        self.v = v

def comparator(x, y):
    if x.w > y.w: return 1
    elif x.w == y.w: return 0
    else: return -1

s = [int(ch) for ch in input().split(' ')]
n, m = s[0], s[1]
w = [int(ch) for ch in input().split(' ')]
v = [int(ch) for ch in input().split(' ')]

ice_creams = []
price = 0
for i in range(len(w)):
    ice_creams.append(IceCream(w[i], v[i]))
    price += v[i]

ice_creams.sort(key=cmp_to_key(comparator))

idx = 0
base_left = 0
for i in range(1, len(ice_creams))[::-1]:
    left = m
    for j in range(i):
        left -= ice_creams[j].v*(ice_creams[i].w-ice_creams[j].w)
        if left < 0: break
    if left >= 0:
        idx = i
        base_left = left

if idx == 0: print(ice_creams[0].w)
else: print(ice_creams[idx].w+base_left//price)

