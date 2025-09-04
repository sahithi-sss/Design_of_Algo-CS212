class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickSelect(l, r):
            pivot, i = nums[r], l

            for j in range(l, r):
                if nums[j] <= pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[r] = nums[r], nums[i]

            if k < i: return quickSelect(l, i-1)
            elif k > i: return quickSelect(i+1, r)
            else: return nums[i]

        return quickSelect(0, len(nums) - 1)
