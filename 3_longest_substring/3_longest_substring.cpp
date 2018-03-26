/*
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. 
Note that the answer must be a substring, "pwke" is a 
subsequence and not a substring.
*/

#include <iostream>
#include <string.h>
#include <unordered_map>
#include <assert.h>

using namespace std;

int longest_substring(string s)
{
	int string_length = s.length();
	if (string_length == 0)
		return 0;

	// map of char, position of char pairs
	std::unordered_map<char, int> unique_chars;

	int start = 0; // start of current sequence
	int end  = 0;  // end of current sequence
	int longest = 0; // longest sequence so far

	for(int i = 0;i <= string_length;i++)
	{
		// in the dict and after the current start
		if (unique_chars.count(s[i])
			&& unique_chars[s[i]] >= start )
		{
			longest = max(longest,i-start);
			start = unique_chars[s[i]] + 1;
		}
		unique_chars[s[i]] = i;
		end = i;
	}

	return max(longest,end-start);
}

void unit_tests()
{
	assert(longest_substring("") == 0);
	assert(longest_substring("a") == 1);

	assert(longest_substring("abcabcbb") == 3);
	assert(longest_substring("bbbbbbb") == 1);
	assert(longest_substring("pwwkew") == 3);
	
	assert(longest_substring("aaabcd") == 4);
	assert(longest_substring("dvdf") == 3);
	assert(longest_substring("jxdlnaaij") == 6);

	cout << "PASS\n";
}

int main(int argc, char const *argv[])
{
	
	if (string(argv[1]) == "-U")
	{
		unit_tests();
	}
	else
	{
		cout << "Longest: " << longest_substring(argv[1]);
	}

	return 0;
}