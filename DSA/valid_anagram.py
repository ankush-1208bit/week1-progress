s = "rat"
t = "car"
if len(s) != len(t):
    print("False")
    exit()
d1 = {}
for i in s:
    if i in d1:
        d1[i] = d1[i] + 1
    else:
        d1[i] = 1
d2 = {}
for j in t:
    if j in d2:
        d2[j] = d2[j] + 1
    else:
        d2[j] = 1
if d1 == d2:
    print("True")
else:
    print("False")