
def get_next(p):
    next = [0 if i != 0 else -1 for i in range(len(p))]
    i, j = 0, -1
    while i < len(p)-1:
        if j == -1 or p[i] == p[j]:
            i += 1
            j += 1
            next[i] = j
        else:
            j = next[j]
    return next


def kmp(t, p):
    next = get_next(p)
    i, j = 0, 0
    while i < len(t) and j < len(p):
        if j == -1 or t[i] == p[j]:
            i += 1
            j += 1
        else:
            j = next[j]
    if j == len(p):
        return i-j
    return -1


t = 'ababababca'
p = 'abababca'

print(kmp(t, p))