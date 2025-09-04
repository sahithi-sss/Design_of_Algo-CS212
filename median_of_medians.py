class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k  # convert to k-th smallest

        def select(arr, k):
            if len(arr) <= 5:
                return sorted(arr)[k]

            # Split into groups of 5
            sublists = [arr[i:i + 5] for i in range(0, len(arr), 5)]
            medians = [sorted(sublist)[len(sublist) // 2] for sublist in sublists]

            # Find pivot using recursive median-of-medians
            pivot = select(medians, len(medians) // 2)

            # Partition
            low  = [x for x in arr if x < pivot]
            equal = [x for x in arr if x == pivot]
            high = [x for x in arr if x > pivot]

            if k < len(low):
                return select(low, k)
            elif k < len(low) + len(equal):
                return pivot
            else:
                return select(high, k - len(low) - len(equal))

        return select(nums, k)
