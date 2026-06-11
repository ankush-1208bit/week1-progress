s = "([)]"
def valid_parenthesis(s):
    pairs = {")": "(","]": "[","}": "{"}
    seen = []
    if len(s) %2 !=0:
        return False
    for i in s:
        if i == "{" or i == "(" or i== "[":
            seen.append(i)
        else:
            last = seen.pop()
            if last != pairs[i]:
                return False
    if len(seen)==0:
        return True
print(valid_parenthesis(s))