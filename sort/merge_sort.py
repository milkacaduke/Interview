
def merge(left_array, right_array):
	"""
		# Complexity: O(n)
	"""
	merged_array = []
	left = 0
	right = 0

	while left < len(left_array) and right < len(right_array):
		if left_array[left] <= right_array[right]:
			merged_array.append(left_array[left])
			left += 1
		else:
			merged_array.append(right_array[right])
			right += 1

	# Take care of left over, should be only 1 left over?
	if len(left_array) != left:
		for i in range(left, len(left_array)):
			merged_array.append(left_array[left])
	if len(right_array) != right:
		for j in range(right, len(right_array)):
			merged_array.append(right_array[right])
	
	return merged_array


def merge_sort(array):
	"""
	# Complexity O(n log(n)) always.
	#		Pro: Always gonna complete in O(n log(n))
	# 	Con: extra space for merging arrayplexity: O(n log(n))
	"""

	# Base Case
	if len(array) <= 1:
		return array

	mid = len(array) // 2
	left = merge_sort(array[:mid])
	
	right = merge_sort(array[mid:])
	

	return merge(left, right)



# driver
import random
result = True
for i in range(1000):
	l = random.sample(range(-100, 100), 99)
	l = merge_sort(l)
	l_correct = sorted(l)
	
	if l != l_correct:
		result = False

if result:
	print("PASS")
else:
	print("FAIL")


# l = [11, 22, 63, 92, 16, 15, 90, 9, 94, 3]
# result = merge_sort(l)
# print(result)

