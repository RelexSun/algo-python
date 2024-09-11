'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''


def longestCommonPrefix(strs):
    if  not strs:
        return ""

    prefix = strs[0] # let prefix be the first element
    for i in strs[1:]: # loop over every element
        while i[:len(prefix)] != prefix: # will iterate until fl == fl
            prefix = prefix[:-1] # keep shorten the prefix
            if not prefix:
                return ""
    return prefix


print(longestCommonPrefix(["flower","flow","flight"]))

word = "flower"
word = word[:-1]
word = word[:-1]
word = word[:-1]
word = word[:-1]
print(word)