c = int(input())
cases = []
for _ in range(c):
    line = [int(ch) for ch in input().split(' ')]
    cases.append(line)
for case in cases:
    nums = case[1:]
    nums.sort()
    res = 0
    for i in range(len(nums)-2):
        res += nums[i]
        nums[i+1] -= nums[i]
        nums[i+2] -= nums[i]
        nums[i] = 0
    print(res)


