nm = list(map(int, input().split(' ')))
n = nm[0]
m = nm[1]
nums = list(map(int, input().split(' ')))
imap = {}
for i in nums:
    if i in imap:
        imap[i] += 1
    else:
        imap[i] = 1
result = nums.copy()
for i in nums:
    if imap[i] > m:
        result.remove(i)
print(''.join(list(map(str, result))))