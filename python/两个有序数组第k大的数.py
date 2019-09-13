

def findKthSmallestNumber(nums1, nums2, k, low1, high1, low2, high2):

    mid1 = (low1+high1) // 2
    mid2 = (low2+high2) // 2
    if low1 <= high1:
        if k 