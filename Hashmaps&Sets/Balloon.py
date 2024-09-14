'''
Given a string text,
you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once.
Return the maximum number of instances that can be formed.

Example 1:
Input: text = "nlaebolko"
Output: 1

Example 2:
Input: text = "loonbalxballpoon"
Output: 2

Example 3:
Input: text = "leetcode"
Output: 0
'''
from collections import defaultdict


def maxNumberOfBalloons(text):
    counter = defaultdict(int)
    balloons = 'balloon'
    for c in text:
        if c in balloons:
            counter[c] += 1
    print(counter)
    for c in balloons:
        if c not in counter:
            return 0
    return min(counter['b'], counter['a'], counter['l']//2, counter['o']//2, counter['n'])


print(maxNumberOfBalloons("loonbalxballpoon"))

