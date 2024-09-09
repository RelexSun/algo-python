from traceback import print_tb

A = [1, 2, 3]
print(A)

print(len(A)) # Check length of array - O(1)

# Append - Insert element at end of array - On average: O(1)
A.append(4)

# Pop -Deleting element at end of aray - O(1)
A.pop()

# Insert (not at the end of array) - O(n)
A.insert(2, 5)

#  Modify an element - O(1)
A[0] = 7

# Accessing element given index i - O(1)
print(A[2])

if 7 in A: print(True)

#  Strings
# Append to end of strings - O(n)
s = 'hello'
b = s + 'z'

print(b)

#  Check if something is in the string - O(n)
if 'e' in s:
    print(True)

# Access positions
print(s[2])