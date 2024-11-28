from itertools import product
a="0123456789AB"
comb=product(a,repeat=5)
c=0
for i in comb:
    s=''.join(i)
    n=s.count('7')
    m=s.count("9")
    x=s.count('A')
    y=s.count("B")
    if s[0]!="0" and n==1 and (x+y+m<=3):
         c+=1
print(c)