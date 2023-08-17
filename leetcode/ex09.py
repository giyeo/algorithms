# https://leetcode.com/problems/palindrome-number

"""
Two-Pointer Approach:
	This approach involves using two pointers, one starting from the beginning of the string and the other starting from the end.
	Move the pointers towards each other while comparing the characters at their positions.
	If the characters are not the same at any point, the string is not a palindrome.
	This approach has a time complexity of O(n), where n is the length of the string.
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        len_x = len(str_x)
        pA = 0
        pB = len_x - 1
        for i in range(len_x // 2):
            if(str_x[pA + i] != str_x[pB - i]):
                return False
        return True
