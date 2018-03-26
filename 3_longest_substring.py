'''
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. 
Note that the answer must be a substring, "pwke" is a 
subsequence and not a substring.
'''


def longest_substring_1(s):

	# letters_seen = {}
	# cur_substring = ''
	longest_substring = ''

	def longest_substring_helper(s,cur_substring,letters_seen):

		nonlocal longest_substring

		if not s:
			# if the last substring is the longest sequence
			if len(longest_substring) < len(cur_substring):
				longest_substring = cur_substring
			return

		for letter in s:

			if letter in letters_seen:

				if len(longest_substring) < len(cur_substring):
					longest_substring = cur_substring
				letters_seen = {}
				letters_seen[letter] = True
				cur_substring = letter
			else:
				cur_substring += letter
				letters_seen[letter] = True

			longest_substring_helper(s[1:],cur_substring,letters_seen)

	longest_substring_helper(s,'',{})

	#print(longest_substring)
	return longest_substring

def longest_substring(s):

	longest_substring = ''
	cur_substring = ''
	letters_position_seen = {}

	for letter in s:

		if letter in letters_position_seen:

			if len(longest_substring) < len(cur_substring):
				longest_substring = cur_substring

			position = letters_position_seen[letter]
			cur_substring = cur_substring[position+1:] + letter
			letters_position_seen = {}
			for position,sub_letter in enumerate(cur_substring):
				letters_position_seen[sub_letter] = position
		else:
			new_position = len(cur_substring)
			cur_substring += letter
			letters_position_seen[letter] = new_position

	if len(longest_substring) < len(cur_substring):
		longest_substring = cur_substring

	return len(longest_substring)

def unit_tests():

	assert longest_substring('') == 0
	assert longest_substring('a') == 1

	assert longest_substring('abcabcbb') == 3
	assert longest_substring('bbbbbbb') == 1
	assert longest_substring('pwwkew') == 3

	assert longest_substring('aaabcd') == 4
	assert longest_substring('dvdf') == 3
	assert longest_substring('jxdlnaaij') == 6

	print('PASS')

def main():
	unit_tests()

if __name__ == '__main__':
	main()