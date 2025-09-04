
def sortArray(nums):
	# normalising 
	max_nums = max(nums)
	nums = [num / (max_nums+1) for num in nums]

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

	# denormalising
	nums = [int(num * (max_nums+1)) for num in nums]
	return nums