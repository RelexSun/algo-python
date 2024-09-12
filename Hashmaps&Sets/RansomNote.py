'''
Given two strings ransomNote and magazine, return true
if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true
'''

def canConstruct(ransomNote, magazine):
    counter = {}
    for letter in magazine: # Loop through magazine let it be m
        if letter in counter:
            counter[letter] += 1 # count every duplicate key if there is and store the value in counter dic
        else:
            counter[letter] = 1 # set default value

    for c in ransomNote: # Loop through ransome let it be n
        if c not in counter: # check to find if a note exist in counter
            return False
        elif counter[c] == 1: # if encounter a key with 1 value which means we've used up all the note so we should delete it
            del counter[c]
        else:
            counter[c] -= 1 # delete a value of a key which means it is used
    return True

# Time: O(m + n)
# Space: O(1) cuz there are 26 different entries all lowercase



# hashmaps or dictionary

'''
other way: shorter but this is not ideal for interview
    from collections import Counter
    1. counter = Counter(magazine) 
    ===============================
    2. counter = defaultdict(int)
        for c in magazine:
            counter[c] += 1
'''
