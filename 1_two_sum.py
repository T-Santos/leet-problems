'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

# def find_sum_offsets(numbers,target):
# 	for (x,number1) in enumerate(numbers):
# 		for (y,number2) in enumerate(numbers):
# 			if y <= x:
# 				continue
# 			if number1+number2 == target:
# 				print(x,y)
# 				return [x,y]

def find_sum_offsets(numbers,target):

	results = {}
	for pos, number in enumerate(numbers):
		find = target - number
		if find in results:
			return [results[find],pos]
		results[number] = pos

def unit_tests():
	assert find_sum_offsets([2,2],4) == [0,1], "4 is not [0,1]"
	assert find_sum_offsets([2,7,11,15],9) == [0,1], "9 is not [0,1]"
	print('PASS')

def main():
	unit_tests()

if __name__ == '__main__':
	main()