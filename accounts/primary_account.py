def two_sum(nums, target):
	"""Return the indices of two numbers that add up to target."""
	seen = {}
	for index, value in enumerate(nums):
		complement = target - value
		if complement in seen:
			return [seen[complement], index]
		seen[value] = index
	return []
