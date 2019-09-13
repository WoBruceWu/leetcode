
def quick_sort(nums, low, high):
    if low < high:
        pivot_pos = partion(nums, low, high)
        quick_sort(nums, low, pivot_pos-1)
        quick_sort(nums, pivot_pos+1, high)


def partion(nums, low, high):
    pivot = nums[low]
    while low < high:
        while low < high and nums[high] > pivot:
            high -= 1
        nums[low] = nums[high]
        while low < high and nums[low] < pivot:
            low += 1
        nums[high] = nums[low]
    nums[low] = pivot
    return low


nums = [4, 3, 2, 1]
quick_sort(nums, 0, len(nums)-1)
print(nums)