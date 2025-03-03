'''
Leetcode - 242. Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
'''
def isAnagram(s:str, t:str) -> bool:
    if len(s) != len(t):
        return False
    hash_dict = dict()
    for c in s:
        hash_dict[c] = hash_dict.get(c, 0) + 1
    for c in t:
        if c in hash_dict:
            hash_dict[c] -= 1
            if hash_dict[c] < 0:
                return False
        elif c not in hash_dict:
            return False
    return True

# Compare two dictionary
def isAnagram(s:str, t:str) -> bool:
    if len(s) != len(t):
            return False

    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    return countS == countT
