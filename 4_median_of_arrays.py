'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0

Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

'''
import math

def find_median(nums1,nums2):

	def median_helper(nums):

		if len(nums) % 2 == 0:
			off1 = int(len(nums)/2)-1
			off2 = int(math.ceil(len(nums)/2))
			val = math.fsum([nums[off1],nums[off2]])/2
			return val
		else:
			val = float(nums[int(len(nums)/2)])
			return val

	if (not nums1
		and not nums2):
		return 0.0

	if not nums1:
		return median_helper(nums2)

	if not nums2:
		return median_helper(nums1)

	pos_nums1 = 0
	pos_nums2 = 0

	half_list = []
	half_list_length = int((len(nums1)+len(nums2))/2)+1
	
	#TODO: This could be done with just pointers to the last correct offsets
	# rather than building a list and just using the last two interesting offsets
	for position in range(half_list_length):

		if pos_nums1 >= len(nums1):
			half_list.append(nums2[pos_nums2])
			pos_nums2+=1
			continue

		if pos_nums2 >= len(nums2):
			half_list.append(nums1[pos_nums1])
			pos_nums1+=1
			continue

		if nums1[pos_nums1] < nums2[pos_nums2]:
			half_list.append(nums1[pos_nums1])
			pos_nums1+=1
		else:
			half_list.append(nums2[pos_nums2])
			pos_nums2+=1	

	if ((len(nums1)+len(nums2)) % 2) == 0:
		return median_helper(half_list[-2:])
	else:
		return median_helper(half_list[-1:])

def unit_tests():

	assert find_median([],[1]) == 1.0, "find_median([],[1]) == 1.0"
	assert find_median([],[2,3]) == 2.5, "find_median([],[2,3]) == 2.5"
	assert find_median([1,3],[2]) == 2.0, "find_median([1,3],[2]) == 2.0"
	assert find_median([1,2],[3,4]) == 2.5, "find_median([1,2],[3,4]) == 2.5"
	assert find_median([1,2],[1,2,3]) == 2.0, "find_median([1,2],[1,2,3] == 2.0"
	assert find_median([1,1,3,3],[1,1,3,3]) == 2.0, "find_median([1,1,3,3],[1,1,3,3]) == 2.0"
	print("PASS") 

def main():
	unit_tests()
	pass

if __name__ == '__main__':
	main()