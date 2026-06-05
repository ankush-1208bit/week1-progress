nums = [3,3]
target = 6
seen = {}
for i in range(len(nums)):
    needed = target - nums[i]
    if needed in seen:
        print([seen[needed], i])
        break
    seen[nums[i]] = i