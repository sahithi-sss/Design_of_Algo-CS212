def sortArray(self, nums: List[int]) -> List[int]:
	N = 10
	buckets = [[] for _ in range(N)]

	for num in nums:
    	buckets[int(num * N)].append(num)
	i = 0
	for bucket in buckets:
    	bucket.sort()
    	for ele in bucket:
			nums[i] = ele
			i += 1

	return nums
