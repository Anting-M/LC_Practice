'''
Leetcode - 49.Group Anagrams
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Explanation:
There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:
Input: strs = [""]
Output: [[""]]
'''
from collections import defaultdict

def groupAnagrams(strs:list[str]) -> list[list[str]]:
    hashtable = {}
    for word in strs:
        word_ordered = ''.join(sorted(word))
        if word_ordered in hashtable:
            hashtable[word_ordered].append(word)
        else:
            hashtable[word_ordered] = [word]
    return list(hashtable.values())

def groupAnagrams(strs:list[str]) -> list[list[str]]:
    hashmap = defaultdict(list)
    for s in strs:
        sorted_s = ''.join(sorted(s))
        hashmap[sorted_s].append(s)
    return list(hashmap.values())
