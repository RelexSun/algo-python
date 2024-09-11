# Hashsets
s = set()

# Add item into Set - O(1)
s.add(1)
s.add(2)
s.add(3)

print(s)

# lookup if item in set - O(1)
if 1 in s:
    print(True)

# Remove item into Set - O(1)
s.remove(3)
print(s)

string = 'aaaassddddfffffffdss'
sett = set(string) # Set construction - O(S) - S is the length of the string

print(sett) # only contain unique values

# Loop over items in set - O(n)
for x in sett:
    print(x)

# Hashmaps - Dictionaries
d = {'greg': 1, 'steve': 2, 'rob': 3}
print(d)

# Add key:value in dictionary: O(1)
d['arsh'] = 4
print(d)

# Check for presence of key in dictionary: O(1)
if 'greg' in d:
    print(True)

# Check the value corresponding to a key in the dictionary: O(1)
print(d['greg'])

# Loop over the key:val pairs of the dictionary: O(n)
for key, val in d.items():
    print(f"key {key}: val {val}")

# Default dic
'''
If you try to access or modify a key that doesn’t exist in the dictionary, 
instead of raising a KeyError, it automatically creates a new entry with a default value.
'''
from collections import defaultdict
default = defaultdict(int)
default2 = defaultdict(list)
print(default[2])

unique_items = defaultdict(set)

items = [("fruit", "apple"), ("fruit", "banana"), ("fruit", "apple"), ("vegetable", "carrot"), ("vegetable", "spinach")]
for category, item in items:
    unique_items[category].add(item)

print(unique_items)

# Counter
from collections import Counter # count how many times key occurred (this is a cheat)
counter = Counter(string)
