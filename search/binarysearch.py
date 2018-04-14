def binarySearch(array, left, right, x):
	
	while right >= left:
		mid = left + (right - left) // 2;

		if array[mid] == x: # found it
			return mid
		elif x < array[mid]: # <- 
			right = mid - 1
		elif x > array[mid]:
			left = mid + 1

	return False




# main
array = [4,35,2,6,3,66,45,8,1,34,78,43,23,22]
array.sort()
print(array)
print(" ", end="")
for i in range(len(array)):
	print("{}, ".format(i), end="")
x = 5
result = binarySearch(array, 0, len(array)-1, x)
print(result)