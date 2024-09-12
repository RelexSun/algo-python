'''
Given two strings s and t, return true if t is an
anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
'''
from collections import Counter
def isAnagram(s, t):
    if len(s) != len(t):
        return False
    s_dict = Counter(s)
    t_dict = Counter(t)
    return s_dict == t_dict



print(isAnagram("anagram", "nagaram"))


'''
other way: 
    1. return sorted(s) == sorted(t)
'''