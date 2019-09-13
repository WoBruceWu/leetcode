s = input().split(' ')
n, k = int(s[0]), int(s[1])

s = input().split(' ')
h = [int(ch) for ch in s]

min_sum = 0

for i in range(k):
    min_sum += h[i]

last_sum = min_sum
idx = 0
for start in range(1, n-k+1):
    sum = (last_sum-h[start-1]+h[start+k-1])
    last_sum = sum
    if sum < min_sum:
        min_sum = sum
        idx = start

print(idx+1)