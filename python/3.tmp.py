class Heap:

    def heapify(self, nums):
        for idx in range(len(nums)//2)[::-1]:
            self.sift_down(nums, idx)
                
    def sift_up(self, nums, idx):
        parent_idx = (idx-1)//2
        while nums[parent_idx] > nums[idx]:
            nums[parent_idx], nums[idx] = nums[idx], nums[parent_idx]
            parent_idx = idx

    def sift_down(self, nums, idx):
        while idx*2 + 1 < len(nums):
            l_idx = idx * 2 + 1
            r_idx = idx * 2 + 2
            min_idx = l_idx
            if r_idx < len(nums) and nums[r_idx] < nums[min_idx]:
                min_idx = r_idx
            if nums[min_idx] < nums[idx]:
                nums[idx], nums[min_idx] = nums[min_idx], nums[idx]
                idx = min_idx
            else:
                break

    def heap_pop(self, nums):
        res = nums[0]
        nums[0], nums[-1] = nums[-1], nums[0]
        nums.pop()
        self.sift_down(nums, 0)
        return res

heap = Heap()
nums = [5,3,1,2,4]

heap.heapify(nums)
for i in range(len(nums)):
    print(heap.heap_pop(nums))
