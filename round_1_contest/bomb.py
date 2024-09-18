# def can_destroy_all_bases(bases, n, k, r):
#     # Start placing bombs from the first base
#     bombs_used = 0
#     i = 0
#     while i < n:
#         bombs_used += 1
#         # Place a bomb such that it covers as many bases as possible
#         bomb_position = bases[i] + r
#         # Move i to the last base that can be destroyed by this bomb
#         while i < n and bases[i] <= bomb_position + r:
#             i += 1
#         # If we exceed k bombs, return False
#         if bombs_used > k:
#             return False
#     return True
#
#
# def minimum_bomb_power(n, k, bases):
#     # Sort the base positions
#     bases.sort()
#
#     # Binary search on the answer: the minimum power r
#     left, right = 0, (bases[-1] - bases[0]) // 2
#     result = right
#
#     while left <= right:
#         mid = (left + right) // 2
#         if can_destroy_all_bases(bases, n, k, mid):
#             result = mid  # Try to minimize r
#             right = mid - 1
#         else:
#             left = mid + 1
#
#     return result
#
#
# # Input reading
# n, k = map(int, input().split())
# bases = list(map(int, input().split()))
#
# # Find and print the minimum bomb power
# print(minimum_bomb_power(n, k, bases))

def exploded_num(start: int, direction: int) -> int:
	radius = 1
	prev = start
	while True:
		next_ = prev
		# Get the furthest explosion index without exceeding the current radius
		while (
			0 <= next_ + direction < len(bales)
			and abs(bales[next_ + direction] - bales[prev]) <= radius
		):
			next_ += direction

		# We didn't find a new haybale, so the chain explosion is over
		if next_ == prev:
			break

		# Update our previous explosion and increment radius
		prev = next_
		radius += 1
	return abs(prev - start)


max_exploded = 0
for i in range(len(bales)):
	# Get the number of exploded bales for the left & right side
	max_exploded = max(max_exploded, exploded_num(i, -1) + exploded_num(i, 1) + 1)
print(max_exploded, file=open("angry.out", "w"))
