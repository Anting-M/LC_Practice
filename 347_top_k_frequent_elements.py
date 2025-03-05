'''
Leetcode - 347.Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
'''

def topKFrequent(self, nums: list[int], k: int) -> list[int]:
    # dictionary to count 
    count = {}
    # Initialize my bucket, the length of nums + 1
    freq = [[] for i in range(len(nums) + 1)]

    # count the frequency
    for n in nums:
        count[n] = 1 + count.get(n, 0)

    # put things into the bucket, n -> number, c -> count
    for n, c in count.items():
        freq[c].append(n)

    res = []
    # Go through the list in reverse order, since we want top K value
    for i in range(len(freq)-1, 0, -1): 
        # Go through freq[i] since it is a list contain the nums have same count
        for num in freq[i]:
            res.append(num)
            if len(res) == k:
                return res

    