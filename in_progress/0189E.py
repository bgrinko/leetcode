# TODO: NEED REFACTORING

nums = [1, 2, 3, 4, 5, 6, 7]
k = 8
k = k % len(nums)
print(k)

for i in range(k):
    e = nums.pop()
    nums.insert(0, e)

print(nums)
