'''
Given an integer array nums of size n, return the number with the value closest to 0 in nums.
If there are multiple answers, return the number with the largest value.

Example 1:

Input: nums = [-4,-2,1,4,8]
Output: 1
Explanation:
The distance from -4 to 0 is |-4| = 4.
The distance from -2 to 0 is |-2| = 2.
The distance from 1 to 0 is |1| = 1.
The distance from 4 to 0 is |4| = 4.
The distance from 8 to 0 is |8| = 8.
Thus, the closest number to 0 in the array is 1.
Example 2:

Input: nums = [2,-1,1]
Output: 1
Explanation: 1 and -1 are both the closest numbers to 0, so 1 being larger is returned.
'''

# This is just finding the smallest number in the array
def findClosestNumber(nums):
    closest = nums[0]
    for i in nums:
        if (abs(i) < abs(closest)) or (abs(i) == abs(closest) and i > closest):
            closest = i

    return closest

print(findClosestNumber([-4,-2,1,4,8]))
print(findClosestNumber([2,-1,1]))


'''
- another good solution
min = abs(nums[0])
nnum = nums[0]
for n in nums:
    d = abs(n)
    if d<min:
        min = d
        nnum= n
        
if nnum<0 and abs(nnum) in nums:
    return abs(nnum)
else:
    return nnum
'''




