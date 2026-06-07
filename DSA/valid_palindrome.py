s = "A man, a plan, a canal: Panama"
def palindrome(s):
    clean = ""
    for i in s:
        if i.isalnum():
            clean += i
    clean = clean.lower()
    n = len(clean)
    for j in range(n//2):
        if (clean[j] != clean[n-1-j]):
            return False
    return True
print(palindrome(s))