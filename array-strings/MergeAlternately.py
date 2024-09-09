'''

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1.
If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string.

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q
merged: a p b q c   d

'''


def mergeAlternately(word1, word2):
    word3 = ''
    word4 = ''
    array = []

    if len(word1) > len(word2):
        word3 = word2
        word4 = word1
    else:
        word3 = word1
        word4 = word2

    last = abs(len(word1) - len(word2))
    if last > 0:
        word5 = word4[-last:]
    else:
        word5 = ''

    for i in range(len(word3)):
        array.append(word1[i])

        array.append(word2[i])
    return "".join(array) + word5

w1 = "abc"
w2 = "pqr"
print(mergeAlternately(w1, w2))
