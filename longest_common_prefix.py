strs = ["a"]       
p = strs[0]
for c in strs[1:]:
    l = min(len(p), len(c))
    t = ""
    for j in range(l):
        if p[j] == c[j]:
            t += p[j]
        else:
            break
    p = t
    if len(p)==0:
        break
print(p)