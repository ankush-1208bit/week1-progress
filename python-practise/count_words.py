s = input("Enter a string: ")
count = 1
for i in s:
    if i.isspace():
        count += 1
print("Total number of words = ", count)