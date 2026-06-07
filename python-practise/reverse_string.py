s = input("Enter a string: ")
rev = ""    
n = len(s)
for i in range(n):
    rev += s[n-1-i]
print("Reversed String:" , rev)