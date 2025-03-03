'''
Leetcode - 217. Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: trueß
Explanation:
The element 1 occurs at the indices 0 and 3.
'''

def containsDuplicate(nums:list[int]) -> bool:
    hashset = set()
    for n in nums:
        if n not in hashset:
            hashset.add(n)
        else:
            return True
    return False

# Slightly clearner without explicit else
def containDuplicate(nums:list[int]) -> bool:
    hashset = set()
    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False
    