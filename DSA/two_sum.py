nums = [2, 7, 11, 15]
target = 9
result  = []
for i in range(len(nums)):
    for j in range(len(nums)):
        if i != j and nums[i] + nums[j] == target:
            result.append(i)
            result.append(j)
            break
    if result:
        break
print(result)    