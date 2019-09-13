class Heap:
    # def heapify(self, nums):
    #     # O(nlogn)时间复杂度
    #     for i in range(len(nums)):
    #         self.sift_up(nums, i)

    def heapify(self, nums):
        # O(n)时间复杂度
        for i in range((len(nums)-1)//2+1)[::-1]: self.sift_down(nums, i)

    def sift_up(self, nums, index):
        parent_index = (index-1)//2
        while nums[parent_index] > nums[index]:
            nums[parent_index], nums[index] = nums[index], nums[parent_index]
            parent_index = index

    def heap_pop(self, nums):
        if len(nums) == 0: return
        if len(nums) == 1: return nums.pop()
        res = nums[0]
        nums[0], nums[-1] = nums[-1], nums[0]
        nums.pop()
        self.sift_down(nums, 0)
        return res

    def sift_down(self, nums, index):
        child1_index = index * 2 + 1
        child2_index = index * 2 + 2
        while child1_index < len(nums):
            child_min_index = child1_index
            if child2_index < len(nums):
                child_min_index = child1_index if nums[child1_index] <= nums[child2_index] else child2_index
            if nums[index] > nums[child_min_index]:
                nums[index], nums[child_min_index] = nums[child_min_index], nums[index]
                index = child_min_index
                child1_index = index * 2 + 1
                child2_index = index * 2 + 2
            else: break


if __name__ == '__main__':
    import heapq
    heap = [2,3,1]
    heapq.heapify(heap)
    while heap:
        print(heapq.heappop(heap))


# class Heap:
#
#     def heapify(self, nums):
#         for idx in range(len(nums) // 2)[::-1]:
#             self.sift_down(nums, idx)
#
#     def sift_up(self, nums, idx):
#         parent_idx = (idx - 1) // 2
#         while nums[parent_idx] > nums[idx]:
#             nums[parent_idx], nums[idx] = nums[idx], nums[parent_idx]
#             parent_idx = idx
#
#     def sift_down(self, nums, idx):
#         while idx * 2 + 1 < len(nums):
#             l_idx = idx * 2 + 1
#             r_idx = idx * 2 + 2
#             min_idx = l_idx
#             if r_idx < len(nums) and nums[r_idx] < nums[min_idx]:
#                 min_idx = r_idx
#             if nums[min_idx] < nums[idx]:
#                 nums[idx], nums[min_idx] = nums[min_idx], nums[idx]
#                 idx = min_idx
#             else:
#                 break
#
#     def heap_pop(self, nums):
#         res = nums[0]
#         nums[0], nums[-1] = nums[-1], nums[0]
#         nums.pop()
#         self.sift_down(nums, 0)
#         return res

