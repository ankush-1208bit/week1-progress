s = "rat"
t = "car"
def valid_anagram(s,t):
    if len(s) != len(t):
        return False
    d = {}
    for i in s:
        if i in d:
            d[i] = d[i] + 1
        else:
            d[i] = 1
    for j in t:
        if j in d:
            d[j] = d[j]-1
            if d[j]<0:
                return False
        else:
            return False
    return True
print(valid_anagram(s,t))