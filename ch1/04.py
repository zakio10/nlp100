s="Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
l = s[:-1:].split(" ")
ans={}

for i in range(len(l)):
    if i in [0, 4, 5, 6, 7, 8, 14, 15, 18]:
        ans[l[i][0]] = i+1
    else:
        ans[l[i][1]] = i+1

print(ans)