# https://leetcode.com/problems/two-sum

"""
Hash Map (or Hash Table) Approach:
	This approach is efficient and has a time complexity of O(n).
	It involves iterating through the array once while storing each number and its index in a hash map.
	As you iterate through the array, you can check if the complement of the current number
	(i.e., the target sum minus the current number) exists in the hash map. If it does, you've found a valid pair.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_ind = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in nums_ind:
                return [nums_ind[complement], i]
            nums_ind[num] = i
        return []