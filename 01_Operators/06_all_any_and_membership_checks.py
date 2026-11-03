nums = [3, 6, 9, 12]

print(all(i % 3 == 0 for i in nums))
print(any(i > 10 for i in nums))
print(6 in nums)
print(7 not in nums)