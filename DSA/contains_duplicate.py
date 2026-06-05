nums = [1,2,3,]
seen = set()
for i in nums:
    if i in seen:
        print("true")
        break
    seen.add(i)
else:
    print("False")