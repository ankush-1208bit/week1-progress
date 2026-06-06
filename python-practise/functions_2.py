#function to find square
def square(n):
    return n*n
# function to check even
def is_even(n):
    if n%2==0:
        return True
    else:
        return False
#function to find largest of two number

def largest(a,b):
    if a>b:
        return a
    else:
        return b
a = int(input("Enter a number to find square:"))
b = int(input("Enter a number to check if its even"))
print(f"Square = {square(a)}, checking even: {is_even(b)}, checking largest{largest(a,b)}")